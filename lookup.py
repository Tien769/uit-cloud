import sys
from operator import add
from pyspark.sql import SparkSession
from datetime import datetime, timedelta


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing arguments")
        sys.exit(-1)


    date = datetime.strptime(sys.argv[1], '%d/%m/%Y')
    delta = timedelta(days=7)
    low = date - delta
    high = date + delta

    spark = SparkSession\
            .builder\
            .appName("app")\
            .getOrCreate()

    df = spark.read.csv('./charts.csv', header=True)

    query = df.filter((df.date > low) & (df.date < high))
    query = query.select("song","artist","rank")
    query.show(100, truncate=False)

    spark.stop()
