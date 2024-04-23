import json
from src.db.inmemorydb import InMemoryDB
import uuid


exercises = [
    {
        "name": "Barbell Squat",
        "difficulty": "Advanced",
        "body_part": "Legs",
        "description": "The barbell squat is a compound exercise that works the quads, hamstrings, glutes, lower back, and core. It is a staple in any leg workout."
    },
    {
        "name": "Deadlift",
        "difficulty": "Advanced",
        "body_part": "Back",
        "description": "The deadlift is a compound exercise that works the hamstrings, glutes, lower back, and core. It is a staple in any back workout."
    },
    {
        "name": "Bench Press",
        "difficulty": "Intermediate",
        "body_part": "Chest",
        "description": "The bench press is a compound exercise that works the chest, triceps, and shoulders. It is a staple in any chest workout."
    },
    {
        "name": "Pull-up",
        "difficulty": "Intermediate",
        "body_part": "Back",
        "description": "The pull-up is a bodyweight exercise that works the back, biceps, and shoulders. It is a staple in any back workout."
    },
    {
        "name": "Dumbbell Bicep Curl",
        "difficulty": "Beginner",
        "body_part": "Biceps",
        "description": "The dumbbell bicep curl is an isolation exercise that works the biceps. It is a staple in any bicep workout."
    }
]

# Generowanie pięciu losowych UUID
uuids = [str(uuid.uuid4()) for _ in range(5)]
print(uuids)