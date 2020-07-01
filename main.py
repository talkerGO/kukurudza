apiUrl = "https://api.vk.com/method/"
apiV = "5.107"
aT = ""

message1 = "Привет"
message2 = "С днём кукурузы тебя!!!"
picture = "photo490433658_457240724"

print("KUKURUDZA is loading...")

import requests
import random
import time

def makeReq(method, ps = {}):
	reqUrl = apiUrl + method
	ps["access_token"] = aT
	ps["v"] = apiV
	req = requests.get(reqUrl, params = ps)
	try:
		return req.json()["response"]
	except:
		if req.json()["error"]["error_code"] == 14:
			sid = req.json()["error"]["captcha_sid"]
			img = req.json()["error"]["captcha_img"]
			print("Captcha needed: + " + img)
			ps["captcha_sid"] = sid
			ps["captcha_key"] = input("?")
			makeReq(method, ps)
		else:
			print(req.json())
aT = input("Give me your access_token: ")
print("Okay!")
print("Searching your friends...")

try:
	friends = makeReq("friends.get")
except:
	print("Oops...")
	print("Some error...")
	print("Bye, bye ;)")
	input()
	a = 1 / 0

try:
	count = int(friends["count"])
	pcount = int(friends["count"])
except:
	print("Oops...")
	print("Some error...")
	print("Bye, bye ;)")
	input()
	a = 1 / 0

print("Detected " + str(count) + " friends")
if count == 0:
	print("Oops...")
	print("You haven't any friend...")
	print("Bye, bye ;)")
	input()
	a = 1 / 0

print("Starting KUKURUDZA attack!")

for friend in friends["items"]:
	print("Sending to " + str(count) + " from " + str(pcount))
	try:
		makeReq("messages.send", {"user_id": friend, "random_id": random.randint(1000000000, 9999999999), "message": message1})
		time.sleep(random.randint(50, 70)/100)
		makeReq("messages.send", {"user_id": friend, "random_id": random.randint(1000000000, 9999999999), "message": message2})
		time.sleep(random.randint(50, 70)/100)
		makeReq("messages.send", {"user_id": friend, "random_id": random.randint(1000000000, 9999999999), "message": "", "attachment": picture})
	except:
		print("Some error...")
	time.sleep(random.randint(70, 120)/100)
	count = count - 1

print("So...")
print("KUKURUDZA attack is compleated")
print("Enjoy ;)")