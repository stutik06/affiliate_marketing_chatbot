from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# --- SQLite Config ---
DATABASE_URL = "sqlite:///chatbot.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# --- Tables ---

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    prompt = Column(Text)
    response = Column(Text)
    timestamp = Column(DateTime, default=datetime.now)

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    prompt = Column(Text)
    rating = Column(Integer)
    timestamp = Column(DateTime, default=datetime.now)

# Create tables
Base.metadata.create_all(bind=engine)

# --- DB Actions ---

def get_user(username):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    db.close()
    return user

def create_user(username, hashed_password):
    db = SessionLocal()
    if get_user(username):
        db.close()
        return False
    user = User(username=username, password=hashed_password)
    db.add(user)
    db.commit()
    db.close()
    return True

def store_chat(username, prompt, response):
    db = SessionLocal()
    chat = Chat(username=username, prompt=prompt, response=response)
    db.add(chat)
    db.commit()
    db.close()

def get_chat_history(username):
    db = SessionLocal()
    chats = db.query(Chat).filter(Chat.username == username).order_by(Chat.timestamp.desc()).limit(10).all()
    db.close()
    return chats

# --- Feedback & RL Support ---

def store_feedback(username, prompt, rating):
    db = SessionLocal()
    existing = db.query(Feedback).filter(
        Feedback.username == username,
        Feedback.prompt == prompt
    ).first()

    if existing:
        existing.rating = rating  # Update existing
    else:
        fb = Feedback(username=username, prompt=prompt, rating=rating)
        db.add(fb)

    db.commit()
    db.close()

def get_feedback_for_prompt(prompt_text):
    db = SessionLocal()
    feedbacks = db.query(Feedback).filter(Feedback.prompt == prompt_text).all()
    db.close()
    return feedbacks

db_session = SessionLocal
