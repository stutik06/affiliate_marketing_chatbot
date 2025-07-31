# 🤖 Affiliate Marketing Chatbot

A **Streamlit-powered GenAI chatbot** designed to explain **why creatives are crucial in affiliate marketing**. This chatbot uses OpenAI models via OpenRouter API, includes user login, chat history, feedback, and a simulated RL feedback loop to refine responses based on user ratings.

---

## 🔧 Tech Stack

| Component        | Technology                          |
|------------------|--------------------------------------|
| Language         | Python 3.8+                          |
| UI               | Streamlit                            |
| LLM              | OpenAI GPT-4o-mini via OpenRouter    |
| Auth             | bcrypt-based login                   |
| Database         | SQLite                               |
| RL Feedback Loop | Rule-based prompt adjustment         |
| Deployment       | Hugging Face Spaces                  |

---

## 🚀 Features
- 🧑‍💼 **User Signup/Login** with password hashing
- 💬 **Conversational UI** via Streamlit
- 💾 **Chat history** storage with timestamps
- 👍👎 **Feedback buttons** to rate answers
- ♻️ **Reinforcement Learning Simulation** (adjusts prompt if feedback is negative)
- ☁️ **Deployed on Hugging Face Spaces**

---

## 🛠️ Setup Instructions

### ✅ Local Setup

```bash
git clone https://github.com/your-username/affiliate-chatbot.git
cd affiliate-chatbot
python -m venv venv
venv\Scripts\activate   # or source venv/bin/activate (Linux/macOS)
pip install -r requirements.txt




