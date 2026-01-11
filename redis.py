
# This script computes real-time engagement scores per student


import redis        
import pymongo      


# Connect to Redis
r = redis.Redis(host='redis', port=6379, db=0)


# Connect to MongoDB to retreive data 
mongo_client = pymongo.MongoClient("mongodb://mongo:27017")

# Access the 'activities' collection from the 'learntrack' database
activities = mongo_client["learntrack"]["activities"].find()


# Compute engagement score per student
for act in activities:
    
    # Build a Redis key for the student engagement score
    key = f"student:{act['studentId']}:score"
    
    # Assign a weight to the activity:
    # add 5 point for a quiz attemp and 1 point for page view
    score = 5 if act['action'] == 'quiz_attempt' else 1
    
    # Increment  engagement score for each student
    r.incrby(key, score)

# Display scores for each student
for student in range(1, 11):
    key = f"student:S{student}:score"
    print(f"{key} -> {r.get(key)}")
