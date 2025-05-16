from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Gemini API Key
genai.configure(api_key="AIzaSyBstVt-GaSTsSWQSY7sAjtUbCYDINL2bDI")

# Use the correct model name
model = genai.GenerativeModel("models/gemini-1.5-flash-001")



@app.route("/", methods=["GET", "POST"])
def index():
    generated_code = ""
    prompt = ""

    if request.method == "POST":
        prompt = request.form.get("prompt", "").strip()
        if not prompt:
            generated_code = "⚠️ Please enter a prompt."
        else:
            try:
                response = model.generate_content(prompt)
                generated_code = response.text
            except Exception as e:
                generated_code = f"❌ Error: {str(e)}"

    return render_template("index.html", prompt=prompt, generated_code=generated_code)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

