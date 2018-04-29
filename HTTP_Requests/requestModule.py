#python -m pip install requests
import requests
url = "https://www.google.com"
response = requests.get(url)
print(f"request to {url}: status code {response.status_code}")
response.ok #True
response.headers
response.text

print("=====================================")

url = "https://icanhazdadjoke.com/"
#"text/plain" only at webs with API
response = requests.get(
    url,
    headers={"Accept": "text/plain"} #"text/html"

)
print(response.text)

print("------------------------------------")

response = requests.get(
    url,
    headers={"Accept": "application/json"}

)
response_data = response.json()  #type 'dict'
print(response_data['joke'])
print(f"status: {response_data['status']}")