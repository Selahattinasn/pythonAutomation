# To get the contents of a website from Python,
#we can choose the request module,
#which is used for interacting with web services. 

import requests


# If module doesn t exists, we can install it with pip
# pip install requests
# pip3 install requests  ->in macOs

# use get() function to get the content of a website

response=requests.get("http://google.com")


# lets use len() function to cehck response 

print(len(response.text))