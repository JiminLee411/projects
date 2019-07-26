from decouple import config
import requests
import pprint
import csv

# 네이버 API 설정
client_id = config('NAVER_CLIENT_ID')
client_secret = config('NAVER_CLIENT_SECRET')

# 헤더 설정
headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret
}

# 변수 선언
movie_names = []
movie_codes = []
naver_movie_info = {}

# 요청
api_url = 'https://openapi.naver.com/v1/search/movie.json'

# movie.csv 불러오기
with open('movie.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        movie_names.append(row['movieNm'])
        movie_codes.append(row['movieCd'])

for query, movieCd in zip(movie_names, movie_codes):
    # 응답
    response = requests.get(f'{api_url}?query={query}', headers=headers).json()
    information = response['items'][0]
    # 딕셔너리에 네이버 영화 정보 저장
    naver_movie_info[movieCd] = {
        '영화 대표코드': movieCd,
        '링크': information['link'] if response['items'] else None,
        '이미지URL': information['image'] if response['items'] else None,
        '유저 평점': information['userRating'] if response['items'] else None
    }

with open('movie_naver.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['영화 대표코드', '링크', '이미지URL', '유저 평점']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in naver_movie_info.values():
        csv_writer.writerow(item)
    