import requests
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r",type=str,required=True,help="set the wordpress root url (exampele: -r http://192.168.1.123/wordpress",metavar="[wordpress root]")
args = parser.parse_args()
wordpressRoot = args.r

if wordpressRoot[-1]=='/':
    wordpressRoot = wordpressRoot[:-1]

url = wordpressRoot+'/wp-json'

resp = requests.get(url).json()
requestList = []
result = resp['routes']

for r in result:
   endpoints = result[r]['endpoints']
   
   for endpoint in endpoints:
    methods = endpoint['methods']
    
    for method in methods:
        api = {'uri': r,'method':method,'param':endpoint['args']}
        requestList.append(api)


   #print(type(r))

for api in requestList:
    url = wordpressRoot+'/wp-json'+api['uri']
    if '(' in url:
        url = url[:url.index('(')]
        url+='123456789k'

    method = api['method']

    if method=='GET':
        resp = requests.get(url)
        if resp.status_code!=404:
            print('method : %s,url : %s, status_code : %d'%(method,url,resp.status_code))
    elif method=='POST':
        resp = requests.post(url)
        if resp.status_code!=404:
            print('method : %s,url : %s, status_code : %d'%(method,url,resp.status_code))
    elif method=='PUT':
        resp = requests.put(url)
        if resp.status_code!=404:
            print('method : %s,url : %s, status_code : %d'%(method,url,resp.status_code))
    elif method=='PATCH':
        resp = requests.patch(url)
        if resp.status_code!=404:
            print('method : %s,url : %s, status_code : %d'%(method,url,resp.status_code))
    elif method=='DELETE':
        resp = requests.delete(url)
        if resp.status_code!=404:
            print('method : %s,url : %s, status_code : %d'%(method,url,resp.status_code))
    else:
        print(method)
        


