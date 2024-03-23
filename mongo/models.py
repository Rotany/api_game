from mongo.entities import User, FinalScore, Points
from bson import ObjectId

class UserModel:
    def __init__(self, user: User):
        self.email = user.email
        self.password = user.password

    def to_dict(self):
        return {
            "email": self.email,
            "password": self.password
        }

class FinalScoreModel:
    def __init__(self, final_score: FinalScore):
        self.user_id = final_score.user_id
        self.score = final_score.score

    def to_dict(self):
        return {
            "user_id": ObjectId(self.user_id),
            "score": self.score
        }


class PointsModel:
    def __init__(self, points: Points):
        self.user_id = points.user_id
        self.coins = points.coins
        self.level = points.level
        self.time = points.time
        self.hearts = points.hearts
    
    def to_dict(self):
        return {
            "user_id": ObjectId(self.user_id),
            "coins": self.coins,
            "level": self.level,
            "time": self.time,
            "hearts": self.hearts
        }