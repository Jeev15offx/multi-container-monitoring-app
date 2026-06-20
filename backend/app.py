from flask import Flask
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "mysql"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "root123"),
            database=os.getenv("DB_NAME", "appdb")
        )

        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")

        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return {
            "message": "Connected successfully",
            "database": result[0]
        }

    except Exception as e:
        return {
            "error": str(e)
        }, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
