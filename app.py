from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect('finance.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS transactions
                 (id INTEGER PRIMARY KEY, amount REAL, category TEXT, type TEXT, date TEXT)''')
    conn.commit()
    conn.close()

@app.route('/transactions', methods=['GET'])
def get_transactions():
    conn = sqlite3.connect('finance.db')
    cursor = conn.execute("SELECT * FROM transactions ORDER BY date DESC")
    data = [{"id": row[0], "amount": row[1], "category": row[2], "type": row[3], "date": row[4]} 
            for row in cursor.fetchall()]
    conn.close()
    return jsonify(data)

@app.route('/transaction', methods=['POST'])
def add_transaction():
    data = request.json
    conn = sqlite3.connect('finance.db')
    conn.execute("INSERT INTO transactions (amount, category, type, date) VALUES (?, ?, ?, ?)",
                (data['amount'], data['category'], data['type'], datetime.now().isoformat()))
    conn.commit()
    conn.close()
    return jsonify({"message": "Added successfully"}), 201

@app.route('/report/monthly', methods=['GET'])
def monthly_report():
    conn = sqlite3.connect('finance.db')
    cursor = conn.execute("""
        SELECT category, SUM(amount) as total 
        FROM transactions 
        WHERE type='expense' 
        GROUP BY category 
        ORDER BY total DESC
    """)
    data = [{"category": row[0], "total": row[1]} for row in cursor.fetchall()]
    conn.close()
    return jsonify({"report": data})

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
