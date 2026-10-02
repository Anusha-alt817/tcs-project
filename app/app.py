from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    env = os.getenv("APP_ENV")
    db_user = os.getenv("DB_USER")

    return f"""
    Application Running Successfully

    Environment: {env}

    Database User: {db_user}
    """
    return """
Version 2 Application

Environment: production
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)