"""
This is a cralwer source for KB lands in Korea

reference
http://edmundmartin.com/concurrent-crawling-in-python/
http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html

"""
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import aiohttp
import asyncio
import ast
import json
import codecs
from ast import literal_eval
import threading


_url = 'http://nland.kbstar.com/quics?page=B047003&cc=b057597:b057605'

_headers = { "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Host": "nland.kbstar.com",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36",
"Origin": "http://nland.kbstar.com",
"Referer": "http://nland.kbstar.com/quics?page=B047003"
}

_payload_list={
"페이지목록건수": '10',
"페이지번호": '1',
"뉴스일련번호": '',
"메뉴구분": '08',
"뉴스제목내용": '',
"검색조건": '1',
"처리구분": '',
"조회시작일": '20070401', #
"조회종료일": '20070630', #
"메뉴구분1": '0',
"임시조회시작일": '20070401', # 20170419
"임시조회종료일": '20070630'
}

_payload_detail={
#"페이지목록건수": '10',
#"페이지번호": '80', #
"뉴스일련번호": '44882', #여기 뉴스번호 44882~66057
#"메뉴구분": '0',
#"뉴스제목내용": '',
# "검색조건": '1',
#"처리구분": 'News', #
#"조회시작일": '20070401', #20170419
#"조회종료일": '20070630',
# "메뉴구분1": '0',
#"임시조회시작일": '20070401',
#"임시조회종료일": '20070630'
}



"""
목록가져오는 부분에 대한 HTTP POST Request
위의 _payload_list에 메뉴구분(아래 코드 참조)와 날짜를 넣음 그것에 해당하는 기사 목록 가져옴
<option value="0" selected="selected">전체</option>
<option value="01">정책/법규</option
<option value="02">분양/청약</option>
<option value="03">재개발/재건축/리모델링</option>
<option value="04">시세동향</option><option value="05">대출정보</option>
<option value="06">자산관리정보</option><option value="07">기타</option>
<option value="08">주상복합/상가</option><option value="13">신도시/택지개발</option>
<option value="14">공매공고</option><option value="15">보도자료/보고서</option>
<option value="16">시장분석</option><option value="17">테마뉴스</option>
</select>
"""
req = requests.post('http://nland.kbstar.com/quics?page=B047003', data=_payload_list, headers=_headers)
# HTML 소스 가져오기
html = req.text
# print(html.find('근린상가가')) # checked ok


"""
페이지 네비게이션이 필요없는것으로 판단
실제 kb부동산의 기사는 sequence id로 따여있는 구조임
44882~66057의 번호를 따져서 생선되어 있고 44882가  2007년 4월 1일 신일이라는 매체에서 올린 기사가 처음 그리고 최근 66057까지 올라와있음
위에 _payload_detail에 44882부터 66057로 돌리면 모든 기사 크롤링 가능
"""
# 각 뉴스 디테일 화면에 대한 HTTP POST Request
req = requests.post('http://nland.kbstar.com/quics?page=B047003&cc=b057597:b057605', data=_payload_detail, headers=_headers)
# HTML 소스 가져오기
html = req.text





# print(html.find('곤혹스러운 게 아니다'))
# print(html.find('콕 찍어 정답을 말할 수는 없다.'))
# 1	기타	[분양광고] 울산 태화강 신일해피트리	-신일-	2007.04.01	1504
#print(html.find('사업 추진 기간이 길어진다.'))

# soup = BeautifulSoup(html, 'html.parser')
# view_cont = soup.find('div', attrs={'class': 'view_cont'})
# #print(type(view_cont))  # confirmed whether or not its type is tag
# print(view_cont.dl.dt.strong.text) # 타이틀
#
# meta_info = view_cont.dl.dd
#
# for item in meta_info.find_all('strong'):
#     print(item.text) # 분류, 등록일, 조회수
#
# try :
#     # 본문
#     article_txt = soup.find('div', attrs={'class': 'article_txt'})
#     print(article_txt.text)
# except AttributeError as e:
#     pass
#
# # 출처
# source = soup.find('p', attrs={'class': 'source'})
# print(source.text.replace('출처',''))

def remove_unnecessary(str) :
    str = str.replace('\n', ' ')\
        .replace('\r', ' ').replace('\"', ' ')\
        .replace('\,', ' ').replace('\t', ' ')\
        .replace('\”', '').replace('‘','')\
        .replace('’','').replace('\'','')\
        .replace('\.','').replace('“', '') \
        .replace('”', '').replace('~','')
    import re
    parse = re.sub('[-=.#/?:$}]', '', str)
    return parse


def get_test_news(id) :
    print(id)

def get_news(id) :

    print(id)
    news_item =  {}

    _payload_detail_assigned = u"{'뉴스일련번호': '" + str(id) + u"'}"
    _payload_detail_assigned = literal_eval(_payload_detail_assigned)

    req = requests.post('http://nland.kbstar.com/quics?page=B047003&cc=b057597:b057605', verify=False, data=_payload_detail_assigned, headers=_headers)
    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    view_cont = soup.find('div', attrs={'class': 'view_cont'})

    if view_cont is None:
        return

    #print(type(view_cont))  # confirmed whether or not its type is tag

    count = 0

    # print(view_cont.dl.dt.strong.text) # 타이틀
    try :
        news_item['title'] = "\"" +  remove_unnecessary(view_cont.dl.dt.strong.text)+ "\""
        count += 1
    except AttributeError as e:
        print(e)
        pass

    try :
        meta_info = view_cont.dl.dd

        for idx, item in enumerate(meta_info.find_all('strong')):
            # print(item.text) # 분류, 등록일, 조회수
            if idx == 0 :
                news_item['category'] = "\"" +   item.text  + "\""
            if idx == 1 :
                news_item['date'] = "\"" +  item.text + "\""
            if idx == 2 :
                news_item['views_count'] = "\"" +  item.text + "\""
        count += 3
    except AttributeError as e:
        print(e)
        pass


    try:
        # 출처
        source = soup.find('p', attrs={'class': 'source'})
        # print(source.text.replace('출처',''))
        news_item['source'] = "\"" +  source.text.replace('출처', '').replace('-', '').replace(' ', '') + "\""
        count += 1
    except AttributeError as e:
        print(e)
        pass

    try:

        # if news_item['source'] == '조인스랜드':
        #     # 본문
        #     article_txt = soup.find('div', attrs={'class': 'detail'})
        # elif news_item['source'] == '동아일보':
        #     # 본문
        #     article_txt = soup.find('div', attrs={'class': 'article_txt'})
        # else:
        #     # 본문
        #     article_txt = soup.find('div', attrs={'class': 'article_txt'})

        article_txt = None
        for try_item in ['detail', 'article_txt'] :
            article_txt = soup.find('div', attrs={'class': try_item})
            if article_txt is not None:
                break
        # news_item['body_content'] = "\"" + article_txt.text.replace('\n', ' ').replace('\r', ' ').replace(',','\\,').replace('\"', '\\"').replace('\‘', '\\‘') + "\""
        news_item['body_content'] = "\"" \
                                    + remove_unnecessary(article_txt.text) \
                                    + "\""

        count += 1
    except AttributeError as e:
        print(e)
        pass

    # print(count)
    # print(news_item)

    # write_to_file(f, ", ".join(map(str, news_item.values())))
    if count == 6 :
        write_to_file(", ".join(map(str, news_item.values())))

    return news_item


def run_script_with_mutiple_threads():
    with ThreadPoolExecutor(max_workers=16) as  Executor:
        # jobs = [Executor.submit(get_test_news, u) for u in range(66466, 44882, -1)]
        jobs = [Executor.submit(get_news, u) for u in range(66485, 44882, -1)]
        # jobs = [Executor.submit(get_news, u) for u in range(66485, 66460, -1)]


lock = threading.Lock()
# f = open("results.csv", 'a+', encoding='utf-8')
f = open("results.csv", 'w', encoding='utf-8')
f.write("\"title\", \"category\", \"date\", \"views_count\", \"source\", \"body_content\"\n")


def write_to_file(row):
    with lock:
        print(row)
        f.write(row + "\n")

# def write_to_file(f, text):
#     lock.acquire() # thread blocks at this line until it can obtain lock
#     # in this section, only one thread can be present at a time.
#     print >> f, text
#     lock.release()



# for i in range(66466, 44882, -1) :
#     # print(i)
#     # print('{} is running!!'.format(i))
#     get_news(str(i))


# print(get_news('66057'))
# print(get_news('66433'))

# 66440 66438 66433 66416

run_script_with_mutiple_threads()