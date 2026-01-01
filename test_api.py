import requests

base_url = "http://localhost:5000"

# Add transactions
requests.post(f"{base_url}/transaction", json={
    "amount": 500, "category": "Food", "type": "expense"
})
requests.post(f"{base_url}/transaction", json={
    "amount": 2000, "category": "Salary", "type": "income"
})

# Test endpoints
print(requests.get(f"{base_url}/transactions").json())
print(requests.get(f"{base_url}/report/monthly").json())
