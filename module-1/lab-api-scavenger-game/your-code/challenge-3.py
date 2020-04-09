### enter your code below

# Libraries
import requests
import os
import json
import re
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# General variables
load_dotenv()
apikey = os.getenv("GIT_API4")
print("Key get it") if apikey else print("We cann't get the key!! please check the env variables")
url="https://api.github.com/"

#
# Hidden Cold Joke
#

owner="ironhack-datalabs"
repo="scavenger"
path=f"repos/{owner}/{repo}/contents/"
#res=requests.get(url+path,auth=HTTPBasicAuth(apikey, ''))
#print(res)
#data=res.json()

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
        print(f'es interesante: {data[item]["name"]}\n y el path es: {data[item]["path"]}')
        return True
    else:
        #print(f'no es interesante: {data[item]["name"]}\n')
        return False

def get_structure(url_rep,api_key,structure=[]):
    res=requests.get(url_rep,auth=HTTPBasicAuth(api_key, ''))
    print(res)
    if res.status_code!=200:
        print(f"url:{url_rep}\n")
        print(f"header: {header}\n")
    data=res.json()
    for k in range(len(data)):
        if data_element_is_dir(data,k):
            structure.append(data[k]['path'])
            get_structure(url_rep+data[k]['name']+'/',api_key,structure)
        elif data_element_is_interesting(data,k):
            structure.append( {"path": data[k]['path'] ,"nombre":data[k]['name'] })
            return structure
    return structure


url_rep=url+path
api_key=apikey

structure=get_structure(url_rep,apikey)
print(f'esta es la estructura:{structure}\n')

if not structure:
    print("Empty structure")
    
else:
    seleccion=[e for e in structure if type(e)==dict]
    if len(seleccion)==0:
        print("la seleccion esta vacia")
    print(f'la selección fue {seleccion}\n')

# ordenar los nombres

nombres =[ {"ind":int(''.join(re.findall('\d',e['nombre']))) ,"path":e['path']} for e in seleccion]

#print(f'los archivos son {Nombres}\n')
print('\n Ordenandos los nombres \n')

nombre_ord=[]
for k in range(len(nombres)):
    for e in nombres:
        if k==e['ind']:
            nombre_ord.append(e["path"])

print(f'Nombres ordenados: {nombre_ord}\n')
# leer el contenido
print('\n leyendo el contenido \n')

lectura=[]
for e in nombre_ord:
    url_consulta=url+path+e
    res=requests.get(url_consulta,auth=HTTPBasicAuth(apikey, ''))
    print(res)

    if res.status_code!=200:
        print(f"url:{url_consulta}\n")
    data=res.json()
    lectura.append(data['content'])


print(f' lectura sin decodificar: {lectura}\n')
import base64
lectura_dec='  '.join([str(base64.b64decode(e))[2:-3] for e in  lectura])
print(f'lectura decodificada: {lectura_dec}\n')





print("jajajajaja")
