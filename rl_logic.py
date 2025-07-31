
from database import Feedback, db_session

# Save user feedback (👍/👎) to DB
def save_feedback(prompt, response, feedback):
    rating = 1 if feedback == "👍 Yes" else 0
    entry = Feedback(prompt=prompt, response=response, rating=rating)
    db_session.add(entry)
    db_session.commit()

# Adjust prompt based on very basic rules (simulated RL)
def adjust_prompt(user_prompt):
    # You can make this smarter by checking DB feedback history
    if "image" in user_prompt.lower():
        return "Describe the image in a simple way: " + user_prompt
    if "why" in user_prompt.lower():
        return "Answer like you're talking to a beginner: " + user_prompt
    return user_prompt
