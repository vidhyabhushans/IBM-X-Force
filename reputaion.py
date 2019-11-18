import urllib3
from json import loads

http = urllib3.PoolManager()
headers = urllib3.util.make_headers(basic_auth='XXXXXXXXXXXXXXXXXXXXXXXXX:XXXXXXXXXXXXXXXXXXX')
api_end = "https://api.xforce.ibmcloud.com/"

def make_req(args):
        res = http.request('GET', api_end + args, headers=headers)
        return(res)

option = input("Enter the number to select the option\n1. Get IP reputation\n2. Get URL reputaion\n3. Get Domain reputation\n4. Get File hash reputation\n")
if option == "1":
        ip = input("Enter IP\n")
        res = make_req("ipr/history/" + ip)
        data = loads(res.data)
        score = data["history"][0]["score"]
        print("Your IP reputation score is:", score)
        print("\n\nFor more information you can refer below link of IBM XForce\nhttps://exchange.xforce.ibmcloud.com/api/doc/?#IP_Reputation_get_ipr_ip\n")
elif option == "2":
        url = input("Enter URL\n")
        res = make_req("url/" + url)
        data = loads(res.data)
        score = data['result']['score']
        print("Your URL's reputation score is:", score)
        print("\n\nFor more information you can refer below link of IBM XForce\nhttps://exchange.xforce.ibmcloud.com/api/doc/?#URL_get_url_url\n")
elif option == "3":
        domain = input("Enter domain\n")
        res = make_req("resolve/" + domain)
        ip = loads(res.data)['A'][0]
        res = make_req("ipr/history/" + ip)
        data = loads(res.data)
        score = data["history"][0]["score"]
        print("Your domain's score is", score)
        print("\n\nFor more information you can refer below link of IBM XForce\nhttps://exchange.xforce.ibmcloud.com/api/doc/?#DNS_get_resolve_input \nhttps://exchange.xforce.ibmcloud.com/api/doc/?#IP_Reputation_get_ipr_ip\n")
elif option == "4":
        file_hash = input("Enter file hash\n")
        res = make_req("malware/" + file_hash)
        data = loads(res.data)
        print(data)
        print("\n\nFor more information you can refer below link of IBM XForce\nhttps://exchange.xforce.ibmcloud.com/api/doc/?#Malware_get_malware_filehash\n")
