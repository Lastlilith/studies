import redis
import mysql.connector
import json

r = redis.Redis(host="localhost", port=6379, db=0)

db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="mydatabase"
)
cursor = db.cursor()

while True:
    message = r.brpop("messages", timeout=0)
    if message:
        message_data = json.loads(message[1])
        cursor.execute(
            "INSERT INTO messages (message) VALUES (%s)",
            (message_data["message"],),
        )
        db.commit()
        print(f"Inserted: {message_data['message']}")
