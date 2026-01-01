# finance-tracker-api
Personal finance REST API with Flask + SQLite
# Personal Finance Tracker API 💰📈

REST API to track income/expenses + spending analytics.

## Live Demo
curl http://localhost:5000/transactions

## Features
- POST income/expenses
- GET spending reports by category/month
- Pie charts JSON data
- SQLite database (no setup)

## Quick Start
pip install flask flask-cors
python app.py
curl -X POST http://localhost:5000/transaction -d '{"amount":500,"category":"Food"}' -H "Content-Type: application/json"

text

**🚀 Deploy:** Railway.app/Heroku (free)
