from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Import CSV Exercise').getOrCreate()

authors = spark.read.csv('authors.csv', sep = ',', inferSchema = True, header = True)
