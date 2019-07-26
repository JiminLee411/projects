import requests
import pprint
import csv
from datetime import datetime, timedelta
from decouple import config

key = config('MOVIE_KEY')
targetDt = '20190713' # yyyymmdd
week = '0'
# per = {}
total = {}
for i in range(50):
    api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb={week}'
    print(api_url)
    response = requests.get(api_url).json()
    targetDt = datetime.strptime(targetDt, '%Y%m%d').date()
    targetDt += timedelta(days=-7)
    targetDt = targetDt.strftime('%Y%m%d')

#     for j in range(10):
#         if response['boxOfficeResult']['weeklyBoxOfficeList'][j]['movieCd'] not in movieCd:
#             audiAcc.append(int(response['boxOfficeResult']['weeklyBoxOfficeList'][j]['audiAcc']))
#             movieCd.append(response['boxOfficeResult']['weeklyBoxOfficeList'][j]['movieCd'])
#             movieNm.append(response['boxOfficeResult']['weeklyBoxOfficeList'][j]['movieNm'])
#             per['영화제목'] = movieNm[-1]
#             per['영화코드'] = movieCd[-1]
#             per['누적순위'] = audiAcc[-1]            
#             total[(i+1)*j] = per

    for movie in response['boxOfficeResult']['weeklyBoxOfficeList']:
        if movie['movieCd'] not in total.keys():
            total[movie['movieCd']] = {
                'movieCd': movie['movieCd'],
                'movieNm': movie['movieNm'],
                'audiAcc': movie['audiAcc']
            }
print(total)

with open('boxoffice.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['movieCd', 'movieNm', 'audiAcc']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in total.values():
        csv_writer.writerow(item)