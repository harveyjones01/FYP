from json.tool import main
import re
import requests
from bs4 import BeautifulSoup

def get_data():

    headers = {
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    url = 'https://uk.investing.com/crypto/bitcoin/historical-data'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    arr =re.findall(r'<td(.*?)</td>', str(soup))
    data = []
    for i in range(5):
        data.append(float(fill_in_data(i+1, arr)))
    return data


def fill_in_data(i, arr):
    n = re.findall(r'data-real-value=(.*?)>', arr[i])
    n = n[0].replace('"', '')
    n = n.replace(',', '0')
    return n

