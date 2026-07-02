from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "project": "SkillSync AI",
        "message": "Backend is running successfully 🚀",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    app.run(debug=True)