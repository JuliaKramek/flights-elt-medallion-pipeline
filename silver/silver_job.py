from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Silver Layer") \
    .master("local[*]") \
    .getOrCreate()

print("Starting Silver layer")

df = spark.read.csv(
    "archive-2/travelverse-dataset.csv",
    header=True,
    inferSchema=True
)

df = df.dropDuplicates()

df.write.mode("overwrite").parquet("/opt/project/silver/output")

print("Silver completed")

spark.stop()