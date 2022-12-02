
import requests
from requests import exceptions 
import re
#此程序作用是判断网站是否是中文网站

#判断字符串是否包含中文
def str_contain_chinese(str):
    for ch in str:
        if u'\u4e00'<=ch<=u'\u9fff':
            return True
    return False

def get_url(url):

    c=False
    
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        }  # 构造请求头
    
    try:
        page=requests.get(url,headers=headers,timeout=3)
        page.encoding='utf-8'
        c = str_contain_chinese(page.text)

    except exceptions.Timeout as e:
        print('error')
    except exceptions.HTTPError as e:
        print('error')
    except:
        print('error')
    else:
        if page.status_code == 200:

            print('ok')
        else:
            print('none')

    return c

pattern = re.compile(
    r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\.'
    r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'
)

def is_valid_domain(value):
    """ 
    Return whether or not given value is a valid domain.
    If the value is valid domain name this function returns ``True``, otherwise False
    :param value: domain string to validate
    """
    return True if pattern.match(value) else False
# 识别前的网站



fi=open('adult.txt','r')

headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        }  # 构造请求头
content =requests.get('https://raw.githubusercontent.com/v2ray/domain-list-community/master/data/category-porn',headers=headers)

fi.write(content)

txt=fi.readlines()

list1=[]
for w in txt:    
    w=w.replace('\n','')
    if(is_valid_domain(w)):
        list1.append(w)
#print(list1)


# 识别后的网站
list2 = []
for url in list1:

    eurl = r'http://'+url
    
    if(get_url(eurl)):
        list2.append(url)
    #print(get_url(eurl))



f=open("chadult.txt","w")
 
for line in list2:
    f.write(line+'\n')
f.close()



