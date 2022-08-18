import json
import requests
import argparse
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--ip",help="please enter the ip adrress using argumanet -i")
    args=parser.parse_args()
    ip=args.ip
    ip=str(ip)
    url="http://ip-api.com/json/"+ip
    response=requests.get(url)
    out=json.loads(response.content)
    print("IP ADDRESS LOCATED")
    print("\t[+] IP\t\t\t",out["query"])
    print("\t[+] CITY\t\t",out["city"])
    print("\t[+] ISP\t\t\t",out["isp"])
    print("\t[+] LOCATION\t\t",out["country"])
    print("\t[+] TIME\t\t",out["timezone"])
    print("\t[+] ZIP\t\t\t",out["zip"])
    print("\t[+] LAT\t\t\t",out["lat"])
    print("\t[+] LON\t\t\t",out["lon"])










