# enter your code below

# Libraries
import requests
import os
import json
from dotenv import load_dotenv


# General variables
load_dotenv()
apikey = os.getenv("GITHUB_API_KEY")
print("Key get it") if apikey else print("We cann't get the key!! please check the env variables")
url="https://api.github.com/"

#
# 1. how many commits where made in the past week
#

path="repos/ironhack-datalabs/datamad0320/commits"
re_params={
        "since":"2020-03-05T00:00:00Z",
        "until":"2020-04-05T23:59:59Z"
        }

# If apiKey is defined, pass a header
headers = {"Authorization":f"token {apikey}"} if apikey else {}

res=requests.get(url+path,headers=headers,params=re_params)

print(res)

data=res.json()
print(f'the commits in the pass week (30-Mar -> 5-Apr) were:{len(data)}')




