from database.db import Session, FeedbackModel

def record_feedback(feedback):
    db = Session()
    fb = FeedbackModel(**feedback.dict())
    db.add(fb)
    db.commit()
    return {"status": "Recorded"}