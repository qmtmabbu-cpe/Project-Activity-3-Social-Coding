from ipaddress import ip_address
from urllib import response
import requests



# get the ip of the user#
def get_ip():
    response = requests.get('https://api.ipify.org?format=json').json()
    return response["ip"]
    

#get the information of the user using the ip address"
def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "postal": response.get("postal")
        
        
    }
    print("============================================")
    print("============================================")
    print("This is the Ipv4 of the user: " + ip_address)
    print("============================================")
    print("============================================")
    print("This is the City of the user: " + response.get("city"))
    print("============================================")
    print("============================================")
    print("This is the Country of the user: " + response.get("country_name"))
    print("============================================")
    print("============================================")
    print("This is the Postal code of the user: " + response.get("postal"))
    print("============================================")
    print("============================================")
    




    return location_data





print(get_location())

