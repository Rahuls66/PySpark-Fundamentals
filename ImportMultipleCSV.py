from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Import Multiple CSV Exercise').getOrCreate()

path = ['<filePath1>','<filePath2>']

files = spark.read.csv(path, sep = ',', inferSchema = True, header = True)
