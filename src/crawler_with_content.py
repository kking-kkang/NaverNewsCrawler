import pandas as pd
import requests
from bs4 import BeautifulSoup

# CSV 불러오기
df = pd.read_csv("../data/코스피_201602.csv")

contents = []
press_names = []

headers = {
    "User-Agent": "Mozilla/5.0"
}

for url in df['url']:
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 본문 내용
        article = soup.find("article", id="dic_area")
        content = article.get_text(separator="\n").strip() if article else ""

        # 언론사 이름
        press_img = soup.find("img", class_="media_end_head_top_logo_img")
        press = press_img["alt"].strip() if press_img else ""

        contents.append(content)
        press_names.append(press)

    except Exception as e:
        print(f"[오류] {url} 처리 중 예외 발생: {e}")
        contents.append("")
        press_names.append("")

# DataFrame에 추가
df['press'] = press_names
df['content'] = contents

# 저장
output_path = "../data/results/코스피_201602.csv"
df.to_csv(output_path, index=False, encoding='utf-8-sig')
print("본문 및 언론사 정보 포함 CSV 저장 완료:", output_path)
