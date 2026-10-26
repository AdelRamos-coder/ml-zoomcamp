import json
from urllib.request import Request, urlopen

url = 'http://localhost:9696/predict'

lead = {
    "lead_source": "organic_search",
    "industry": "technology",
    "employment_status": "employed",
    "location": "europe",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0,
    "interaction_count": 7,
    "lead_score": 0.74
}

req = Request(url, data=json.dumps(lead).encode(), headers={'Content-Type': 'application/json'}, method='POST')
with urlopen(req) as resp:
    result = json.load(resp)

print(result)
print(round(result['conversion_probability'], 3))
