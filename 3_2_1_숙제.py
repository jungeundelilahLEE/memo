import requests
from bs4 import BeautifulSoup


# to 멘토님 : headers의 역할이 뭔가요? 여기는 어떤게 들어가야 할까요? :: 부가정보 // 접속한 경로?
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# to 멘토님 : 이부분(data.text, 'html.parser')은 무엇인가요??
# HTML을 BeautifulSoup 이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦

# BeautifulSoup : 기본적으로 패키지 import를 통해서 가져옴
# 웹 데이터 크롤링 또는 스크래핑을 할 때 사용하는 python 라이브러리인 BeautifulSoup
# GET을 요청할 때   ST = requests.get(url주소,)
# POST를 요청할 때  ST = requests.post()
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨


# 순위, 곡 제목, 가수 (rank albumtitle artist)

musicsss = soup.select('tr.list')
# select를 이용해서, tr 불러오기 (tr class = 'list')
# body > div > tbody > tr (흠.. 이거 어떻게 찾는게... 좋을까?? ㅎㅎ)


for music in musicsss:
# musicsss (tr들) 의 반복문

    a_title = music.select_one('a.title')
    a_artist = music.select_one('a.artist')
    a_albumtitle = music.select_one('a.albumtitle')
    # music안에 변수 a 중 title, artist, albumtitle 뽑아내기

    if a_title is not None:
    # music안에 a 가 있으면 : a 의 text 를 print
    # to 멘토님 : 여기 None 자리는 항상 대문자로 써야하나요? (소문자 : 오류)

        print(a_title.text.strip(), a_artist.text, a_albumtitle.text)
        # strip() :공백없애기


rank = 1
for music in musicsss:
    a_title = music.select_one('a.title')
    if a_title is not None:

        rank += 1

        print(rank, a_title.text.strip(), a_artist.text, a_albumtitle.text)


# to 멘토님 : rank 뽑을 때 이렇게 하는 게 맞나요? 출력이 되긴 했는데.. ㅎ




