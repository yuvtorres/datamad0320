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
# 1.  Get the list of forks
#

owner="ironhack-datalabs"
repo="datamad0320"
path=f"repos/{owner}/{repo}/forks"

# If apiKey is defined, pass a header
headers = {"Authorization":f"token {apikey}"} if apikey else {}

res=requests.get(url+path,headers=headers)

#print(res)


data=res.json()
print(len(data))

repos=[repo["forks_url"] for repo in data]
print('\n'.join(repos))

#
# 2. y 3.    Language attribute of each fork and print
#

languages=list({fork['language'] for fork in data})
   
print(languages)


