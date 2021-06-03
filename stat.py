import sys
from operator import add
from pyspark.sql import SparkSession
from datetime import datetime, timedelta


if __name__ == "__main__":
    spark = SparkSession\
            .builder\
            .appName("app")\
            .getOrCreate()

    df = spark.read.csv('./charts.csv', header=True)

    query = df.select("artist","rank").filter(df.rank <= 20)
    query = query.groupBy("artist").count()
    query = query.sort("count", ascending=False)

    query.show()

    spark.stop()
