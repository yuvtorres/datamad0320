### enter your code below

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
# Hidden Cold Joke
#

owner="ironhack-datalabs"
repo="scavenger"

# If apiKey is defined, pass a header
headers =  {"Authorization":f"token {apikey}"} if apikey else {}


path=f"repos/{owner}/{repo}/contents/"
res=requests.get(url+path,headers=headers)
print(res)
data=res.json()

def describe_data(data,item=0):
    print(f"número de elementos en data {len(data)}\n")
    print(f"elemento {item} de data {data[item]}")

def data_element_is_dir(data,item):
    try:
        if data[item]["type"]=='dir':
            return True
        return False
    except:
        print(data)

def data_element_is_interesting(data,item):
    if data[item]["name"].find('.scavengerhunt')!=-1:
        True
    else:
        False

def get_structure(url_rep,header,structure=[]):
    res=requests.get(url_rep,header)
    print(res)
    if res.status_code!=200:
        print(f"url:{url_rep}\n")
        print(f"header: {header}\n")
    data=res.json()
    for k in range(len(data)):
        if data_element_is_dir(data,k):
            structure.append(data[k]['path'])
            get_structure(url_rep+data[k]['name']+'/',header,structure)
        elif data_element_is_interesting(data,k):
            structure.append('is interesting:'+data[k]['path'])
            return structure

url_rep=url+path
header=headers

structure=get_structure(url_rep,header)
structure
