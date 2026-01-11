from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# -----------------------------------
# Create Spark Session
# -----------------------------------
spark = SparkSession.builder \
    .appName("Course Engagement") \
    .config("spark.cassandra.connection.host", "cassandra") \
    .config("spark.mongodb.read.connection.uri",
            "mongodb://mongo:27017/learntrack.activities") \
    .getOrCreate()

# -----------------------------------
# Read data from MongoDB
# -----------------------------------
df = spark.read.format("mongodb").load()

print("=== Records read from MongoDB ===")
print(df.count())
df.show(truncate=False)

# -----------------------------------
# Transform data
# -----------------------------------
df = df.withColumn("date", F.to_date(F.col("timestamp")))

result = df.groupBy("courseId", "date").count() \
           .withColumnRenamed("courseId", "courseid")

print("=== Aggregated course engagement ===")
result.show(truncate=False)

# -----------------------------------
# Write results to Cassandra
# -----------------------------------
result.write \
    .format("org.apache.spark.sql.cassandra") \
    .options(table="course_engagement", keyspace="learntrack") \
    .mode("append") \
    .save()

print("=== Data successfully written to Cassandra ===")

spark.stop()
