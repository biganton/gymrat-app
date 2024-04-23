from .idb import IDB
import json


class InMemoryDB(IDB):
    def __init__(self):
        self.users = []
        self.data_path = "src/db/exercises.json"

        with open(self.data_path, 'r') as file:
            self.exercises = json.load(file)

    def save_data(self):
        data = {
            'exercises': self.exercises
        }
        with open(self.data_path, 'w') as file:
            json.dump(data, file, indent=4)

    def add_user(self, user):
        self.users.append(user)
        return user

    def add_exercise(self, exercise):
        self.exercises.append(exercise)
        self.save_data()
        return exercise

    def delete_exercise(self, exercise_id):
        self.exercises = [ex for ex in self.exercises if ex.id != exercise_id]
        self.save_data()
        return {"message": "Exercise deleted"}

    def get_exercises(self):
        return self.exercises
    
    def add_description(self, description):
        self.exercises.append(description)
        return description
