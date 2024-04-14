import datetime


class User:
    def __init__(
        self, email: str, password: str, username: str
    ):
        self.email = email
        self.password = password
        self.username = username

    def __str__(self):
        return f"{self.email}"

class FinalScore:
    def __init__(
        self, user_id, score
    ):
        self.user_id = user_id
        self.score = score

class Points:
    def __init__(
        self, user_id: str, coins: int, level: int, time: datetime.datetime, hearts: int
    ):
        self.user_id = user_id
        self.coins = coins
        self.level = level
        self.time = time
        self.hearts = hearts
    
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "coins": self.coins,
            "level": self.level,
            "time": self.time,
            "hearts": self.hearts
        }
    