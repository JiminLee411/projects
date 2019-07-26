# 코드로 실제 이미지 저장하는 법
import requests
import csv

# 변수 선언
movie_img_url = []
movie_codes = []

with open('movie_naver.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        movie_img_url.append(row['이미지URL']) # 인터넷 상의 이미지파일 리스터 저장
        movie_codes.append(row['영화 대표코드'])

# 요청 -> 파일 저장
for url, movieCd in zip(movie_img_url, movie_codes):
    with open(f'images/{movieCd}.jpg', 'wb') as f: # wb : 바이너리 파일을 쓰겠다.
        response = requests.get(url)
        f.write(response.content) # 텍스트형식(json, html, xml....)이 아닌 형식을 받을 때는 .content