import requests
response = requests.post("http://192.168.101.3:5000/next")
print(response.status_code, response.text)
