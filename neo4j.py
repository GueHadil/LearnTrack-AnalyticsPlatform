# neo4j_loader.py
from neo4j import GraphDatabase
import pymongo

# -----------------------------------
# Connect to Neo4j (Bolt protocol)
# -----------------------------------
driver = GraphDatabase.driver(
    "bolt://neo4j:7687",
    auth=("neo4j", "Hadildada123")
)

# -----------------------------------
# Connect to MongoDB
# -----------------------------------
mongo_client = pymongo.MongoClient("mongodb://mongo:27017")
activities = mongo_client["learntrack"]["activities"].find()

# -----------------------------------
# Load activities into Neo4j
# -----------------------------------
for act in activities:
    with driver.session() as session:
        session.run(
            """
            MERGE (s:Student {id: $studentId})
            MERGE (r:Region {name: $region})
            CREATE (a:Activity {
                courseId: $courseId,
                timestamp: datetime($timestamp)
            })
            MERGE (s)-[:PERFORMED]->(a)
            MERGE (a)-[:IN_REGION]->(r)
            """,
            studentId=act["studentId"],
            courseId=act["courseId"],
            region=act["region"],
            timestamp=act["timestamp"].isoformat()
        )

print("Activities successfully loaded into Neo4j")

# -----------------------------------
# Multi-region access detection (within 1 hour)
# -----------------------------------
query = """
MATCH (s:Student)-[:PERFORMED]->(a1:Activity)-[:IN_REGION]->(r1:Region),
      (s)-[:PERFORMED]->(a2:Activity)-[:IN_REGION]->(r2:Region)
WITH s, r1, r2, duration.between(a1.timestamp, a2.timestamp) AS d
WHERE r1.name <> r2.name
  AND abs(d.seconds) / 60 < 30
RETURN s.id AS studentId,
       collect(DISTINCT r1.name) + collect(DISTINCT r2.name) AS regions
"""


with driver.session() as session:
    result = session.run(query)
    for record in result:
        print(record)

# -----------------------------------
# Close Neo4j connection
# -----------------------------------
driver.close()
