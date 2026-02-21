# Databricks notebook source
dbutils.widgets.removeAll()

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

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

ruta = f"abfss://{container}@{datalake}.dfs.core.windows.net/EcommereceSales2024.csv"

# COMMAND ----------

df_ecommerceSales2024 = spark.read.option('header', True)\
                        .option('inferSchema', True)\
                        .csv(ruta)

# COMMAND ----------

ecommerceSales_schema = StructType(fields=[StructField("user_id", IntegerType(), False),
                                     StructField("product_id", StringType(), True),
                                     StructField("interaction_type", StringType(), True),
                                     StructField("interaction_date", StringType(), True)
])

# COMMAND ----------

# DBTITLE 1,Use user specified schema to load df with correct types
df_ecommerceSales_final = spark.read\
.option('header', True)\
.schema(ecommerceSales_schema)\
.csv(ruta)

# COMMAND ----------

ecommerceSales_renamed_df = df_ecommerceSales_final.withColumnRenamed("user id", "user_id") \
                                            .withColumnRenamed("productId", "product_id") \
                                            .withColumnRenamed("Interaction type", "interaction_type") \
                                            .withColumnRenamed("Time stamp", "interaction_date") 

# COMMAND ----------

# DBTITLE 1,Add col with current timestamp 
ecommerceSales_final_df = ecommerceSales_renamed_df.withColumn("ingestion_date", current_timestamp())

# COMMAND ----------

ecommerceSales_final_df.write.mode("overwrite").saveAsTable(f"{catalogo}.{esquema}.ecommerce_sales")
