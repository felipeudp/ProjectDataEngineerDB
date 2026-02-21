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

ruta = f"abfss://{container}@{datalake}.dfs.core.windows.net/product_details.csv"

# COMMAND ----------

df_productDetails = spark.read.option('header', True)\
                        .option('inferSchema', True)\
                        .csv(ruta)

# COMMAND ----------

product_details_schema = StructType(fields=[StructField("product_id", StringType(), False),
                                     StructField("product_name", StringType(), True),
                                     StructField("brand_name", StringType(), True),
                                     StructField("asin", StringType(), True),
                                     StructField("category", StringType(), True),
                                     StructField("upc_ean_code", StringType(), True),
                                     StructField("list_price", FloatType(), True),
                                     StructField("selling_price", FloatType(), True),
                                     StructField("quantity", FloatType(), True),
                                     StructField("model_number", StringType(), True),
                                     StructField("about_product", StringType(), True),
                                     StructField("product_especification", StringType(), True),
                                     StructField("technical_details", StringType(), True),
                                     StructField("shipping_weight", StringType(), True),
                                     StructField("product_dimensions", StringType(), True),
                                     StructField("image", StringType(), True),
                                     StructField("variants", StringType(), True),
                                     StructField("sku", StringType(), True),
                                     StructField("product_url", StringType(), True),
                                     StructField("stock", IntegerType(), True),
                                     StructField("product_details", StringType(), True),
                                     StructField("dimensions", StringType(), True),
                                     StructField("color", StringType(), True),
                                     StructField("ingredients", StringType(), True),
                                     StructField("directions_to_use", StringType(), True),
                                     StructField("is_amazon_seller", StringType(), True),
                                     StructField("size_quntity_variant", StringType(), True),
                                     StructField("product_description", StringType(), True)
                                   ])

# COMMAND ----------

# DBTITLE 1,Use user specified schema to load df with correct types
product_detail_final = spark.read\
.option('header', True)\
.schema(product_details_schema)\
.csv(ruta)

# COMMAND ----------

# DBTITLE 1,Add col with current timestamp 
product_detail_final_df = product_detail_final.withColumn("ingestion_date", current_timestamp())

# COMMAND ----------

product_detail_final_df.write.mode("overwrite").saveAsTable(f"{catalogo}.{esquema}.product_detail")
