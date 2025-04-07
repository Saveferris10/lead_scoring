from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Load your OpenAI API key (set this as an environment variable for security)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Sample GPT prompt template
def generate_prompt(email_text):
    return f"""
    Analyze the following client message and provide:
    1. Overall sentiment (positive/neutral/negative)
    2. Urgency level (low/medium/high)
    3. Buying intent (low/medium/high)
    4. Recommended next action
    5. Lead score from 1 to 10

    Client message:
    "{email_text}"

    Response:
    """

@app.route("/analyze_email", methods=["POST"])
def analyze_email():
    data = request.json
    email_text = data.get("email")
    
    if not email_text:
        return jsonify({"error": "Email text is required"}), 400

    prompt = generate_prompt(email_text)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that evaluates client emails for lead scoring."},
                {"role": "user", "content": prompt}
            ]
        )

        result = response['choices'][0]['message']['content'].strip()
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
