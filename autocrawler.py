import os
import requests
import json
import time
import bs4
from tqdm import tqdm
import random
from wikihow_crawler.crawler import HowToPage

USE_TITLES_DATA = True

user_agents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
]

url = "https://zh.wikihow.com/"
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'User-Agent': "",
    'Connection': 'keep-alive',
    'Referer': 'http://www.baidu.com/'
}


def save_json(data,save_path,mode='w'):
    with open(save_path,mode=mode,encoding='utf-8') as f:
        for line in tqdm(data,desc='saving'):
            json.dump(line,f,ensure_ascii=False)
            f.write('\n')

def load_json(input_path):
    with open(input_path,mode='r',encoding='utf-8') as f:
        data = []
        while True:
            line = f.readline()
            if not line:
                return data
            data.append(json.loads(line))     

# get titles of articles
titles_path = os.path.join("data/data_titles.json")

if not USE_TITLES_DATA and not os.path.exists(titles_path):
    res = requests.get(url,headers=headers)
    time.sleep(random.randint(5,15)+random.uniform(0,1))
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    rs = soup.find("ul",attrs={"id":"hp_categories_list"}).find_all("span")
    cats = [i.get_text() for i in rs]
    print(cats)
    link = []
    for cat in tqdm(cats,desc="Get Titles"):
    # cat = cats[0]
        url_query = url + "Category:" + cat + f"?pg={1}"
        res = requests.get(url_query,headers=headers)
        time.sleep(random.randint(5,15)+random.uniform(0,1))# sleep for some time so that crawler won't be stopped
        soup = bs4.BeautifulSoup(res.text, 'html.parser') 
        pg_num_li = soup.find("ul",class_="pagination")
        if not pg_num_li:
            pg_num = 0
        else:
            pg_num = len(pg_num_li.find_all("li"))
        rs_pg = soup.find_all("div",class_="responsive_thumb_title")
        for k in rs_pg:
            title = k.find("p").get_text()
            if title not in link:
                link.append(title)
        for i in tqdm(range(2,pg_num+1)):
            url_query = url + "Category:" + cat + f"?pg={i}"
            res = requests.get(url_query,headers=headers)
            time.sleep(random.randint(5,15)+random.uniform(0,1))
            soup = bs4.BeautifulSoup(res.text, 'html.parser') 
            rs_pg = soup.find_all("div",class_="responsive_thumb_title")
            for k in rs_pg:
                title = k.find("p").get_text()
                if title not in link:
                    link.append(title)
    save_json([{'titles':link}],save_path=titles_path)
else:
    titles = load_json(titles_path)
    link = titles[0]['titles'][:200]

# start crawling
data = []
start_point = 100
cnt = start_point

for i in tqdm(range(start_point,len(link)),desc="crawling"):
    title = link[i]
    print(f"Query:{title}")
    url_query = url + title

    try:
        rs = HowToPage(url_query)
    except TimeoutError or requests.exceptions.ConnectionError or requests.exceptions.ProxyError:
        print("another try")
        time.sleep(60)
        rs = HowToPage(url_query)
    
    data.append({'title':'如何'+title,'content':str(rs),'url':url_query})
    time.sleep(random.randint(10,25)+random.uniform(0,1))
    cnt += 1
    if cnt % 100 == 0:
        save_json(data,save_path="data/data_{}.jsonl".format(cnt//100))
        data = []
if len(data) > 0:
    save_json(data,save_path="data/data_{}.jsonl".format(1+cnt//100))

# combine data
data = []
for i in range(1,2+cnt//100):
    data_i = load_json("data/data_{}.jsonl".format(i))
    data.extend(data_i)
save_json(data,save_path="data/data.jsonl")

for i in range(1,2+cnt//100):
    os.remove("data/data_{}.jsonl".format(i))
    

