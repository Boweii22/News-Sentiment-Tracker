import requests
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy_host = "brd.superproxy.io"
proxy_port = "33335"
proxy_user = "your_proxy_username"
proxy_pass = "your_proxy_password"

proxies = {
    "http": f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}",
    "https": f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}",
}

# url = "https://geo.brdtest.com/welcome.txt?product=resi&method=native"

# response = requests.get(url, proxies=proxies, verify=False)
response = requests.get("https://httpbin.org/ip", proxies=proxies, verify=False)
print(f"Status: {response.status_code}")
print("The response is ", response.text)
