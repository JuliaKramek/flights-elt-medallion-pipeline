from pyspark.sql import SparkSession

def run_silver():
    print("Running SILVER layer")

    spark = SparkSession.builder \
        .appName("silver-layer") \
        .getOrCreate()

    print("Processing using Spark engine")

    print("Executing silver/load_silver.sql")

    spark.stop()

    print("SILVER finished\n")
