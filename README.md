# lead_scoring
🧠 AI-Powered Lead Scoring Assistant

This project uses GPT-4 and Claude to analyze client emails, assign lead scores, and recommend next-best actions—helping real estate and sales professionals prioritize their outreach.

📦 Tech Stack

Backend: Python, Flask, OpenAI API, Flask-CORS

Frontend: React.js

AI Models: GPT-4 (via OpenAI API)

🚀 Setup Instructions

1. Clone the Repo

git clone https://github.com/your-username/lead-scoring-app.git
cd lead-scoring-app

2. Backend Setup (Flask)

cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Create .env file and add your OpenAI key:
echo "OPENAI_API_KEY=your-key-here" > .env

# Run the server
python app.py

3. Frontend Setup (React)

cd ../frontend
npm install
npm run dev  # or npm start

✨ Features

Analyze emails with GPT-4 and Claude

Get sentiment, urgency, buying intent, lead score

Simple UI with real-time feedback

📬 Example Prompt to GPT

Analyze the following client message and provide:
1. Overall sentiment (positive/neutral/negative)
2. Urgency level (low/medium/high)
3. Buying intent (low/medium/high)
4. Recommended next action
5. Lead score from 1 to 10

Client message:
"Hi, I’m looking to move within the next 2 weeks. I loved the last property you showed me. Can we schedule another tour?"

🔐 Environment Variables

Create a .env file in your /backend directory:

OPENAI_API_KEY=your-key-here

🌐 Deployment Options

Backend: Render, Heroku, or Railway

Frontend: Vercel, Netlify, or GitHub Pages

🙌 Author

Faress Berhe – built with AI, full-stack skills, and vision.

Feel free to fork, improve, and build from this foundation!