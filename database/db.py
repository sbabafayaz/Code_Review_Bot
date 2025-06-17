from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./feedback.db"  # 🔴 Use PostgreSQL in production

Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class FeedbackModel(Base):
    __tablename__ = "feedback"
    suggestion_id = Column(String, primary_key=True)
    decision = Column(String)
    reason = Column(Text)

Base.metadata.create_all(engine)

