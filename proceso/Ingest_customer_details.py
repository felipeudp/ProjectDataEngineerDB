# Databricks notebook source
dbutils.widgets.removeAll()

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType,FloatType, BooleanType
from pyspark.sql.functions import current_timestamp, to_timestamp, concat, col, lit

# COMMAND ----------

dbutils.widgets.text("container", "raw")
dbutils.widgets.text("catalogo", "catalog_project")
dbutils.widgets.text("esquema", "bronze")
dbutils.widgets.text("datalake", "adlssmartdataproject")

# COMMAND ----------

container = dbutils.widgets.get("container")
catalogo = dbutils.widgets.get("catalogo")
esquema = dbutils.widgets.get("esquema")
datalake = dbutils.widgets.get("datalake")

ruta = f"abfss://{container}@{datalake}.dfs.core.windows.net/customer_details.csv"

# COMMAND ----------

customer_detail__schema = StructType(fields=[StructField("customer_id", IntegerType(), False),
                                  StructField("age", IntegerType(), True),
                                  StructField("gender", StringType(), True),
                                  StructField("item_Purchased", StringType(), True),
                                  StructField("category", StringType(), True),
                                  StructField("purchase_amount_USD", IntegerType(), True),
                                  StructField("location", StringType(), True),
                                  StructField("size", StringType(), True), 
                                  StructField("color", StringType(), True),
                                  StructField("season", StringType(), True),
                                  StructField("review_rating", FloatType(), True),
                                  StructField("subscription_status", StringType(), True),
                                  StructField("shipping_type", StringType(), True),
                                  StructField("discount_applied", StringType(), True),
                                  StructField("promo_code_used", StringType(), True),
                                  StructField("previous_purchase", IntegerType(), True),
                                  StructField("payment_method", StringType(), True),
                                  StructField("frecuency_of_purchase", StringType(), True),
                                 
])

# COMMAND ----------

customer_detail_df = spark.read \
            .option("header", True) \
            .schema(customer_detail__schema) \
            .csv(ruta)

# COMMAND ----------

customer_detail_with_timestamp_df = customer_detail_df.withColumn("ingestion_date", current_timestamp())

# COMMAND ----------

customer_detail_with_timestamp_df.write.mode('overwrite').saveAsTable(f'{catalogo}.{esquema}.customer_detail')
