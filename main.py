import random
import string
import threading
import requests

# USE A VPN TO STAY UNDETECTED

# HOW TO FIGHT AGAINST SCAMM SIGN UP PAGES 
# IDENTIFY THE REQUEST URL BY CLICKING SUBMIT BUTTON ON THE FORM AND going to Headers tab and replace that post url request with your one
# GO TO PAYLOAD IF IN CHROME AND TAKE NOTE OF THE CREDENTIALS 
# Replace your params with my one along with the following data like username is the param and data is john
# and then POST using request.post
def spam(username,password):
  url = "https://example.com/" # replace this your scam website's POST URL
  params = {
    'username': '{}'.format(username), # these fields need to be replaced with your own
    'password': '{}'.format(password),

  }
  response = requests.post(url, data=params)
  print(response.status_code)


randomusername = ""
randompassword = ""
# get all the fields , loop through them and set the digits, add a class to set limit on each datatype

def mainspam():
 randomusername = ""
 randompassword = ""
 while True:
     # the implementation of the for loops can be changed for your needs, right now it is designed to generate 10 character username and passwords. 
     for i in range(10):
        randomusername = randomusername + random.choice(string.ascii_letters)



     for j in range(10):
        randompassword = randompassword + random.choice(string.digits) + random.choice(string.ascii_letters)

     print("Fake username {} and fake password {}".format(randomusername,randompassword))
     spam(randomusername,randompassword)
     randomusername = ""
     randompassword = ""

# these threads can be left alone or changed depending on your needs. rememeber to divide your total num of threads by 2 and split up
# example, currently the total num of threads is 200, so divide by 2 is 100, so do 2 seperate for loops with value 100 in both of them. 

threads = []
for i in range(200):
    t = threading.Thread(name=mainspam(),daemon=True)
    threads.append(t)


for i in range(100):
    threads[i].join()


for j in range(100):
    threads[j].join()
