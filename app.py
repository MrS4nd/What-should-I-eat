import requests

url = "https://www.example.com"
response = requests.get(url)

if response.status_code == 200:
    print("Request successful!")
    website_content = response.text
    print(website_content)

else:
    print("Request failed with status code:", response.status_code)
