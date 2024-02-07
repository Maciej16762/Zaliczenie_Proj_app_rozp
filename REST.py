import requests


def get_public_ip():
    url = "https://api.ipify.org/?format=json"
    response = requests.get(url)
    ip = response.json().get("ip", "Nie można uzyskać IP.")
    print(f"Twój publiczny adres IP: {ip}")

get_public_ip()

