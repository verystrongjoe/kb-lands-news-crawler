# KB 부동산 종합뉴스 크롤러

KB종합뉴스에 있는 조인스랜드, 조선닷컴, 동아일보등 다양한 매체에서 올라오는 기사에 대한 정보 크롤링

## 설정정보
KB 부동산의 경우 실제로 기사별로 sequence ID가 따져있다.  18년 4월 23일 기준으로 66466번쨰 기사 아이디가 채번이 되었기 떄문에 이 번호를 시작으로 하였다. 이후 정보 크롤링시 이부분을 크롬 개발자 도구로 확인하면 되겠다. 그리고 최초의 기사는 44882번부터 시작이므로 참고 


## 크롤 데이터 정보
제목, 카테코리, 등록일자, 조회수, 출처, 본문 내용


## 크롤 버젼

### 기본 크롤러
```
python kb-land-crawler.py
```


### Concurrent.Future (Multi thread version)
멀티 스레드 기반으로 훨씬 빠른 속도로 해당 데이터 전부를 크롤링해올수 있다.
```
python kb-land-crawler-speed-boost.py
```

## 크롤링된 데이터



## Reference

http://edmundmartin.com/concurrent-crawling-in-python/

http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html
