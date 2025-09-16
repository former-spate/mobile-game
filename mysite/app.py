from flask import Flask, request, jsonify, render_template_string
import os
import random

app = Flask(__name__)

# Ensure uploads folder exists
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Serve index.html
@app.route('/')
def index():
    with open("index.html") as f:
        return render_template_string(f.read())

# Endpoint to analyze uploaded photos
@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files.get("photo")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Predefined options
    foundations = ["Light beige", "Medium beige", "Warm ivory", "Golden tan"]
    lipsticks = ["Soft pink", "Coral", "Nude", "Red berry"]
    eyeshadows = ["Neutral brown palette", "Warm gold shimmer", "Rose tones", "Smokey gray"]
    blushes = ["Soft coral", "Peach", "Rosy pink", "Warm bronze"]
    highlighters = ["Champagne glow", "Golden shimmer", "Pearl highlight"]
    eyebrows = ["Define with light brown pencil", "Define with dark brown pencil", "Natural fill"]
    mascaras = ["Lengthening black", "Volumizing brown", "Curling black"]

    # Randomly pick one from each category
    result = {
        "foundation": random.choice(foundations),
        "lipstick": random.choice(lipsticks),
        "eyeshadow": random.choice(eyeshadows),
        "blush": random.choice(blushes),
        "highlighter": random.choice(highlighters),
        "eyebrows": random.choice(eyebrows),
        "mascara": random.choice(mascaras)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
