import requests
while True:
	x = requests.get('https://w3schools.com')
	print(x.status_code)
	print(x.content)