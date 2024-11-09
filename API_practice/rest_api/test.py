import requests 

Base="http://127.0.0.1:5000/"

# response=requests.put(Base+"video/1", {"likes":10, "name":"a", "views":10000})
# print(response.json())
# input()
response=requests.get(Base+"video/6")
print(response.json())