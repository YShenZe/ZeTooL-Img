import requests
from bs4 import BeautifulSoup
import pyfiglet
import random
from fake_useragent import UserAgent
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from colorama import init, Fore

# 佛祖保佑，永无bug
#      ____  
#     /    \ 
#    /      \
#   |        |
#   |  O  O  |  
#   |    ^   |
#   |   ---  |  
#    \______/
#   /        \
#  /__________\
#    |      |
#    |      |
#    |      |
#   (__)  (__)

init(autoreset=True)

art = pyfiglet.figlet_format("ZeTooL-Img")
print(art)

url = input("请输入要爬取的链接: ")

systems = [
    "Windows NT 6.1; Win64; x64",
    "Windows NT 10.0; Win64; x64",
    "Windows NT 6.3; Win64; x64",
    "Android 8.0.0; Pixel 2",
    "Android 9.0.0; Pixel 3",
    "Android 10.0; Pixel 4",
    "iOS 16.0; iPhone 13",
    "iOS 17.0; iPhone 14",
    "iOS 18.0; iPhone 15"
]
system = random.choice(systems)

ip = f"223.104.{random.randint(0, 255)}.{random.randint(0, 255)}"
ua = UserAgent()
user_agent = ua.random

headers = {
    "User-Agent": user_agent,
    "X-Forwarded-For": ip,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
}

retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[500, 502, 503, 504, 404, 403],
    allowed_methods=["HEAD", "GET", "OPTIONS"]
)

session = requests.Session()
session.mount("http://", HTTPAdapter(max_retries=retry_strategy))
session.mount("https://", HTTPAdapter(max_retries=retry_strategy))

def fetch_page(url):
    try:
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.Timeout:
        print(Fore.RED + "错误: 请求超时，请检查网络连接或稍后重试。")
        return None
    except requests.exceptions.TooManyRedirects:
        print(Fore.RED + "错误: 请求的URL出现重定向过多的情况。")
        return None
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(Fore.RED + "错误: 找不到页面 (404)。请检查URL是否正确。")
        elif response.status_code == 403:
            print(Fore.RED + "错误: 权限不足 (403)。访问被拒绝。")
        else:
            print(Fore.RED + f"HTTP 错误: {http_err}")
        return None
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"请求出错: {e}")
        return None

response = fetch_page(url)
if response is None:
    print(Fore.RED + "无法爬取该链接，请检查URL或稍后再试。")
else:
    soup = BeautifulSoup(response.text, 'html.parser')

    image_links = []
    video_links = []

    for img_tag in soup.find_all('img'):
        img_src = img_tag.get('src')
        if img_src:
            if not img_src.startswith('http'):
                img_src = url + img_src
            image_links.append(img_src)
            print(Fore.GREEN + f"[Fetch Log] Image Link: {img_src}")

    for video_tag in soup.find_all('video'):
        video_src = video_tag.get('src')
        if video_src:
            if not video_src.startswith('http'):
                video_src = url + video_src
            video_links.append(video_src)
            print(Fore.GREEN + f"[Fetch Log] Video Link: {video_src}")
        
        for source_tag in video_tag.find_all('source'):
            source_src = source_tag.get('src')
            if source_src:
                if not source_src.startswith('http'):
                    source_src = url + source_src
                video_links.append(source_src)
                print(Fore.GREEN + f"[Fetch Log] Video Link: {source_src}")

    with open('media_links.txt', 'w', encoding='utf-8') as file:
        file.write('--- Image Links ---\n')
        for img_link in image_links:
            file.write(img_link + '\n')
        
        file.write('\n--- Video Links ---\n')
        for video_link in video_links:
            file.write(video_link + '\n')

    print(Fore.GREEN + '链接已经保存到 media_links.txt 文件中。')
