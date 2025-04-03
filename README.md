# NaverNewsCrawler
키워드랑 날짜 설정해서 네이버 뉴스 크롤링하기 2025ver
# 📰 네이버 뉴스 크롤러 (한 달 단위 수집용)

이 프로젝트는 네이버 뉴스에서 `코스피`, `코스닥` 관련 뉴스를 **월 단위로 수작업 크롤링**하기 위해 학부생들이 직접 수행할 수 있도록 구성된 Python 기반 도구입니다.

크롤링된 결과는 CSV 파일로 저장되며, **한 달에 하나의 파일만 수집**함으로써 **정확하고 품질 높은 데이터 확보**를 목표로 합니다.

---

## <사전 준비>

### 1. Python 3.10 이상 설치

- [Python 다운로드](https://www.python.org/downloads/)

### 2. Chrome 설치 및 ChromeDriver 준비

- 본인 Chrome 버전 확인: `chrome://version`
- [ChromeDriver 다운로드](https://googlechromelabs.github.io/chrome-for-testing/)
    - 크롬 버전에 맞는 드라이버를 다운로드
    - `chromedriver.exe` 를 아래 두 가지 방식 중 하나로 설정

## ChromeDriver 설정 방법 (Windows 기준)

▶ 방법 1: 시스템 환경변수(PAT‌H)에 chromedriver 경로를 등록해 전역 실행 가능하게 만들기

시스템 환경변수 편집 → PATH 항목에 해당 경로 추가

`내 컴퓨터 > 속성 > 고급 시스템 설정 > 환경 변수`

그 후 코드에서 경로 지정 없이 바로 사용 가능

▶ 방법 2: `naver_news_crawler.ipynb`와 같은 폴더에 `chromedriver.exe`를 두고 경로 지정

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")

# chromedriver.exe가 main.py와 같은 폴더에 있는 경우
service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
```

---

## <크롤링 설정>

크롤링에 사용할 키워드와 날짜는 코드 상단에서 직접 설정합니다.

예시

```python
keyword = "코스피"
start_date = ("2016", "1", "1")
end_date = ("2016", "1", "31")
```

설정한 `keyword`와 `start_date` 값을 기준으로, 저장 파일명 **{keyword}_{YYYYMM}.csv**
예시: 코스피_201601.csv
