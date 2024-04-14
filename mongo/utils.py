
def document_to_user(document) -> dict:
    return {
        "_id": str(document["_id"]),
        "email": document["email"]
    }

def document_to_final_score(document) -> dict:
    return {
        "_id": str(document["_id"]),
        "user": document_to_user(document["user"]),
        "score": document["score"]
    }

def document_to_points(document) -> dict:
    print(document)
    return {
        "_id": str(document["_id"]),
        "user": document_to_user(document["user"]),
        "coins": document["coins"],
        "level": document["level"],
        "time": document["time"],
        "hearts": document["hearts"]
    }