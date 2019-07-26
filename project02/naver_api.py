from decouple import config
import requests

# 네이버 API 설정
client_id = config('NAVER_CLIENT_ID')
client_secret = config('NAVER_CLIENT_SECRET')

# 헤더 설정
headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret
}

# 요청
api_url = 'https://openapi.naver.com/v1/search/movie.json'
query = '자전차왕 엄복동'

# 응답
response = requests.get(f'{api_url}?query={query}', headers=headers).json()

print(response)
