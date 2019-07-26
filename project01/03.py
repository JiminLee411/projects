import requests
import pprint
import csv
from datetime import datetime, timedelta
from decouple import config

key = config('MOVIE_KEY')
movieCdes = list()
i = 0
peopleTotalInfo = {}
peoples = []
with open('movie.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        peoples.append(row['peopleNm'])
        
# print(peoples)

for peopleNm in peoples:        
    api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}&peopleNm={peopleNm}'
    response = requests.get(api_url).json()     
    pprint.pprint(response)
    people_info = response['peopleListResult']['peopleList']
    if '감독' == people_info[0]['repRoleNm'] and peopleNm == people_info[0]['peopleNm']:
        peopleTotalInfo[peopleNm] = {
            'peopleNm': people_info[0]['peopleNm'] if people_info[0] else None,
            'peopleCd': people_info[0]['peopleCd'] if people_info[0] else None,
            'repRoleNm': people_info[0]['repRoleNm'] if people_info[0] else None,
            'filmoNames': people_info[0]['filmoNames'] if people_info[0] else None,
        }
# pprint.pprint(peopleTotalInfo)

with open('director.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['peopleNm', 'peopleCd', 'repRoleNm', 'filmoNames']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in peopleTotalInfo.values():
        csv_writer.writerow(item)