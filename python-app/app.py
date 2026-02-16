from flask import Flask, request, jsonify
import psycopg2
import os
import time

app = Flask(__name__)

DB_HOST = os.getenv("DATABASE_HOST")
DB_NAME = os.getenv("DATABASE_NAME")
DB_USER = os.getenv("DATABASE_USER")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")

# Wait for DB to be ready
def get_db_connection():
    while True:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            return conn
        except:
            print("Waiting for database...")
            time.sleep(2)

# Create table if not exists
conn = get_db_connection()
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id SERIAL PRIMARY KEY,
        content TEXT NOT NULL
    );
""")
conn.commit()
cur.close()
conn.close()

@app.route("/")
def home():
    return "Python Flask App with PostgreSQL is running!"

@app.route("/add", methods=["POST"])
def add_message():
    data = request.json
    message = data.get("message")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (content) VALUES (%s)", (message,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"status": "Message added"}), 201

@app.route("/messages", methods=["GET"])
def get_messages():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, content FROM messages;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
