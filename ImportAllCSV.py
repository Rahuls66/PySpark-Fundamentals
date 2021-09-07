from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Import All CSV Exercise').getOrCreate()

f2 = spark.read.csv('*csv', sep = ',', inferSchema = True, header = True)
