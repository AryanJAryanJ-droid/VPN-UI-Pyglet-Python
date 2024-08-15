import requests

index = 0
connectionOn = ['Status: INTERNET CONNECTED']
connectionOff = ['Status: INTERNET DISCONNECTED']

url = "https://www.google.com/"
timeout = 10           
def check():
    try:
        retuests = requests.get(url, timeout=timeout)
        print("Internet is on")
        return connectionOn
            
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("Internet is off")
        return connectionOff
            
    