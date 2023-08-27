'''
Part of this code was taken from https://github.com/HelloChatterbox/PyWikiHow/blob/dev/pywikihow/__init__.py

sudo apt-get install wkhtmltopdf

https://pypi.org/project/pdfkit/
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

https://github.com/HelloChatterbox/PyWikiHow/blob/dev/pywikihow/__init__.py
'''
import random
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
USER_AGENT = random.choice(user_agents)

url = "https://zh.wikihow.com/"
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'User-Agent': USER_AGENT,
    'Connection': 'keep-alive',
    'Referer': 'http://www.baidu.com/'
}


import os
import requests
import bs4
import pdfkit
from tqdm import tqdm

class Crawler :
    url_lang = {
        # 'en' : 'https://wikihow.com/wikiHowTo?search=',
        "zh" : "https://zh.wikihow.com/wikiHowTo?search="
    }
    
    def __init__(self, language) :
        if language in Crawler.url_lang :
            self.url = Crawler.url_lang[language]
        else :
            self.url = Crawler.url_lang['en']
    
    def search(self, query, resultset = [], n = 10) :
        if not query.strip() :
            return resultset
        query = query.replace(' ', '+')
        page = 0
        while n > 0 :
            rs = self.__request_query(query, page)
            for r in rs :
                if r not in resultset :
                    try :
                        how_to = HowToPage(r)
                        resultset.append(how_to)
                        n -= 1
                        if n <= 0 :
                            break
                    except :
                        pass
            page += 1
        return resultset

    def __request_query(self, query, page = 0) :
        url_query = self.url+query+f"&start={15*(page)}"
        try:
            res = requests.get(url_query)
        except TimeoutError or requests.exceptions.ConnectionError:
            raise TimeoutError
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        rs = soup.find_all('a', class_ = "result_link", href=True)
        links = []
        for r in rs :
            links.append(r['href'])
        return links

class HowToPage :
    def __init__(self, url):
        self.url = url
        self.__parse()
        
    def save_pdf(self, path = './') :
        name = self.url[self.url.rfind('/')+1:].replace(' ', '') + '.pdf'
        lang = 'en'
        if 'pt.' in self.url :
            lang = 'pt'
        elif 'es.' in self.url :
            lang = 'es'
        name = f"{lang}-{name}"

        self.filename = name
        full_path = os.path.join(path, name)
        if not os.path.isfile(full_path) :
            pdfkit.from_url(self.url, full_path)
            # r = pdfkit.PDFKit(self.url, 'url', options=None, toc=None, cover=None,configuration=None, cover_first=False, verbose=False)
            # print(123)
            # r.to_pdf(full_path)

    
    def __str__(self) :
        ret = ''
        if self.title :
            ret += self.title
        
        if self.intro :
            ret += '\n' + self.intro
        
        if self.steps :
            for s in self.steps :
                ret += '\n' + s   

        return ret

    def __parse(self) :
        headers['User-Agent'] = random.choice(user_agents)
        res = requests.get(self.url,headers=headers)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        self.__parse_title(soup)
        self.__parse_intro(soup)
        self.__parse_steps(soup)
        #print(res.json)

    def __parse_title(self, soup) :
        tag =soup.find_all('h1', class_=["title_lg", "title_md", "title_sm"])[0]
        self.title = tag.text

    def __parse_intro(self, soup) :
        self.intro = ""
        html = soup.find('div', class_="mf-section-0")
        if html :
            super = html.find("sup")
            if super != None:
                for sup in html.findAll("sup"):
                    sup.decompose()
                    intro = html.text
                    self.intro = intro.strip()
            else:
                intro = html.text
                self.intro = intro.strip()

        

        
    
    def __parse_steps(self, soup) :
        self.steps = []
        step_html = soup.findAll("div", {"class": "step"})
        count = 0
        for html in step_html:
            # This finds and cleans weird tags from the step data
            sup = html.find("sup")
            script = html.find("script")
            if script != None:
                for script in html.findAll("script"):
                    script.decompose()
            if sup != None:
                for sup in html.findAll("sup"):
                    sup.decompose()
            count += 1
            sum_html = html.find("b")
            if sum_html :
                summary = sum_html.text
                for _extra_div in sum_html.find_all("div"):
                    summary = summary.replace(_extra_div.text, "")
            else :
                summary = html.text

            
            ex_step = html
            for b in ex_step.findAll("b"):
                b.decompose()
            desc = ex_step.text.strip()
            s = f"{count} - {summary} {desc}"
            
            self.steps.append(s)
            #self.steps.append(step)
            
    def __eq__(self, other) :
        if isinstance(other, str) :
            return self.url == other
        elif isinstance(other, HowToPage) :
            return self.url == other.url
        else :
            return False
    



