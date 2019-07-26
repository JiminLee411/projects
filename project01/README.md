# Project 01

**목표**

* 기초 Python에 대한 이해한다.
* Python을 통한 데이터 수집 및 파일 저장한다.
* Python 조건/반복문 및 다양한 자료구조 조작한다.
* API 활용을 통해 데이터를 수집하고 내가 원하는 형태로 가공한다.
* 영화평점사이트에 필요한 데이터를 프로그래밍을 통해 수집한다.

**영화진흥위원회 오픈 API**

* [영화진흥위원회의 open API](http://www.kobis.or.kr/kobisopenapi/homepg/user/openLogin.do) 에 로그인을 한다.
* 키 발급/관리 카테고리에서 키 발급을 받는다.
* Open API카테고리의 제공서비스 카테고리에서 원하는 정보의 URL 및 활용 방식을 찾는다.



### 1. 주간/주말 박스오피스 데이터(영화진흥위원회 오픈 API)

1. 주간(월~일)까지 기간의 데이터를 조회한다.

   * [영화진흥위원회의 open API](http://www.kobis.or.kr/kobisopenapi/homepg/user/openLogin.do) 사이트를 이용하여 데이터를 조회한다.

   * 기본 요청 url : http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.xml (또는 .json) 을 이용하여 필요한 요청 url을 작성한다.

   * ![1563769515577](C:\Users\student\Desktop\과제\1563769515577.png)

   * ![1563769569985](C:\Users\student\Desktop\과제\1563769569985.png)

     ```python
     import requests
     
     key = '___'
     targetDt = '20190713'
     week = '0' # 주간 박스오피스 데이터 요청 값
     # 요청할 url주소 제작
     ## key, targetDt, weekGb를 추가하여 주간 기간의 데이터를 조회하기 위한 url주소를 제작한다.
     api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb={week}'
     
     # json형식으로 문서를 요청 받는다.
     response = requests.get(api_url).json() 
     ```

2. 50주간의 데이터를 조회한다.

   * datetime 함수를 이용하여 날짜 단위로 연산을 한다.
   * `striptime`  : 연산을 위해 string형식의 `targetDt` 값을 변경한다.
   * `strftime` : url에 보낼 string형식으로 변형한다.

   ```python
   from datetime import datetime, timedelta
   
   for i in range(50):
       api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb={week}'
       
       response = requests.get(api_url).json()
       
       # 연산을 위한 형식으로 변형한다.
       targetDt = datetime.strptime(targetDt, '%Y%m%d').date() 
       # 7일의 빼는 연산을 해준다.
       targetDt += timedelta(days=-7)
       # string 형식으로 변형한다.
       targetDt = targetDt.strftime('%Y%m%d')
   ```

3. 조회한 한 주의 데이터에서 필요한 데이터를 뽑아낸다.

   - dictionary를 이용하여 `movieCd` , `movieNm` , `audiAcc` 의 value를 뽑아낸다.

   ```python
   for movie in response['boxOfficeResult']['weeklyBoxOfficeList']:
       # 새로운 딕셔너리인 total에 'movieCd'의 값이 없다면 movieCd, movieNm, audiAcc를 추가한다.
       if movie['movieCd'] not in total.keys():
           total[movie['movieCd']] = {
                   'movieCd': movie['movieCd'],
                   'movieNm': movie['movieNm'],
                   'audiAcc': movie['audiAcc']
           }
   ```

4. 필요한 data를 저장한 dictionary를 boxoffice.csv파일로 저장한다.

   * `with open()` 을 통해 `boxoffiec.csv` 라는 파일을 `w` : write 한다. 
   * field명 지정 : fieldmanes를 list형식으로 지정한다.
   * `csv.DictWriter()` 를 이용하여 딕셔너리 형식으로 저장한다.
   * for 문을 이용하여 한 행씩 저장하여 csv파일을 완성한다.

   ```PYTHON
   with open('boxoffice.csv', 'w', encoding='utf-8') as f:
       fieldnames = ['movieCd', 'movieNm', 'audiAcc']
       csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
       csv_writer.writeheader()
       for item in total.values():
           csv_writer.writerow(item)
   ```

5. **결과**

   **총 186개**

    영화 코드     영화명                            누적관객수                  
   20196309	스파이더맨: 파 프롬 홈	6685160
   20183867	알라딘	10161238
   20184047	토이 스토리 4	3151062
   20185353	기방도령	220182
   20183782	기생충	9919835
   20185986	진범	106756
   20191601	극장판 엉덩이 탐정: 화려한 사건 수첩	101245
   20199951	애나벨 집으로	459037
   20196655	존 윅 3: 파라벨룸	913066
   20192151	미드소마	45707
   20198453	롱 리브 더 킹: 목포 영웅	1076588
   20190273	천로역정: 천국을 찾아서	228365
   20182585	비스트	199009
   20192591	BIFAN2019 판타스틱 단편 걸작선 1	25000
   20192022	마담 싸이코	37437
   20196657	맨 인 블랙: 인터내셔널	843649
   20190885	사탄의 인형	46546
   20182387	엑스맨: 다크 피닉스	860921
   20190466	세상을 바꾼 변호인	31379
   19880001	이웃집 토토로	142372
   20191401	업사이드	30244
   20198291	로켓맨	98703
   20184889	어벤져스: 엔드게임	13887813
   20188941	악인전	3346654
   20184865	고질라: 킹 오브 몬스터	352862
   20199063	빅샤크2: 해저2만리	44189
   20188144	0.0MHz	133522
   20184082	걸캅스	1618601
   20199448	어린 의뢰인	193949
   20198597	교회오빠	65399
   20199822	더 보이	88514
   20187981	배심원들	270270
   20198598	명탐정 피카츄	680420
   20185784	나의 특별한 형제	1462434
   20198183	뽀로로 극장판 보물섬 대모험	752508
   20185384	호텔 뭄바이	61163
   20197503	서스페리아	19684
   20197147	어글리 돌	50816
   20169323	안도 타다오	25540
   20183096	생일	1191113
   20181877	캡틴 마블	5796057
   20060347	판의 미로 - 오필리아와 세 개의 열쇠	482408
   20199736	프렌즈: 둥지탈출	10185
   20183454	요로나의 저주	197125
   20180825	미성년	279305
   20198982	크게 될 놈	90320
   19990220	노팅 힐	49958
   20176103	돈	3388756
   20198104	바이스	131698
   20185406	헬보이	311910
   20182501	왓칭	46139
   20198844	아이 엠 마더	83953
   20196244	샤잠!	636971
   20185352	어스	1450902
   20197423	공포의 묘지	87134
   20183773	장난스런 키스	390548
   20198403	파이브 피트	67395
   20196025	덤보	296253
   20197092	로망	46938
   20198146	콜레트	35223
   20197846	악질경찰	254451
   20175407	우상	175481
   20166301	썬키스 패밀리	26086
   20197483	1919 유관순	46858
   20197283	이스케이프 룸	544462
   20197356	라스트 미션	93476
   20198603	페이트 스테이 나이트 헤븐즈필 제2장 로스트 버터플라이	24340
   20197617	정글북: 마법 원정대	22534
   20184574	그린 북	409871
   20196601	항거:유관순 이야기	1143977
   20182530	극한직업	16243231
   20185881	증인	2519150
   20177539	사바하	2389760
   20196723	숲속왕국의 꿀벌 여왕	18305
   20180937	더 페이버릿: 여왕의 여자	133508
   20177282	리노	16489
   20176442	자전차왕 엄복동	168884
   20195743	신데렐라:마법 반지의 비밀	281705
   20195791	어쩌다, 결혼	70827
   20186261	드래곤 길들이기 3	1498759
   20188282	알리타: 배틀 엔젤	1946206
   20195915	해피 데스데이 2 유	392397
   20020222	해리포터와 비밀의 방	79301
   20185576	콜드 체이싱	78303
   20184888	메리 포핀스 리턴즈	199519
   20174169	기묘한 가족	216254
   20180868	뺑반	1821147
   20162003	명탐정 코난:전율의 악보	83376
   20185478	극장판 헬로카봇: 옴파로스 섬의 비밀	558144
   20185444	레고 무비2	71030
   20184105	말모이	2848736
   20185124	러브 유어셀프 인 서울	342366
   20184896	가버나움	87787
   20176251	내안의 그놈	1910802
   20189463	주먹왕 랄프 2: 인터넷 속으로	1754950
   20182544	글래스	452460
   20186324	언더독	176837
   20185485	보헤미안 랩소디	9910706
   20189385	몬스터 파크	30571
   20180290	아쿠아맨	5019235
   20183915	극장판 공룡메카드: 타이니소어의 섬	379569
   20182588	미래의 미라이	77985
   20186281	범블비	1553491
   20170658	PMC: 더 벙커	1665200
   20175547	스윙키즈	1462873
   20183785	점박이 한반도의 공룡2 : 새로운 낙원	521053
   20184187	언니	172338
   20182421	그린치	543813
   20168773	마약왕	1787825
   20183479	극장판 짱구는 못말려: 아뵤! 쿵후 보이즈 ~라면 대란~	259753
   20183238	스파이더맨: 뉴 유니버스	628327
   20177552	국가부도의 날	3723913
   20179230	도어락	1546002
   20183375	극장판 포켓몬스터 모두의 이야기	86997
   20189843	호두까기 인형과 4개의 왕국	408425
   20182082	부탁 하나만 들어줘	87501
   20178825	모털 엔진	262070
   20183745	런닝맨 : 풀룰루의 역습	180709
   20177538	완벽한 타인	5270621
   20184481	성난황소	1567264
   20181905	후드	276658
   20176814	신비한 동물들과 그린델왈드의 범죄	2403686
   20183073	베일리 어게인	78439
   20181171	바울	229837
   20183007	거미줄에 걸린 소녀	25172
   20182966	투 프렌즈	20419
   20183050	번 더 스테이지: 더 무비	298402
   20182935	출국	71407
   20182669	툴리	24325
   20186822	너의 췌장을 먹고 싶어	48910
   20170513	동네사람들	445625
   20189869	해피 투게더	15745
   20174981	창궐	1588443
   20010291	해리포터와 마법사의 돌	259733
   20179006	여곡성	55997
   20181404	벽 속에 숨은 마법시계	211233
   20180523	스타 이즈 본	458917
   20182693	구스범스: 몬스터의 역습	21400
   20180987	할로윈	90492
   20179189	암수살인	3777611
   20189067	미쓰백	710780
   20182403	크레이지 리치 아시안	147806
   20186321	퍼스트맨	630470
   20177221	베놈	3851409
   20189123	곰돌이 푸 다시 만나 행복해	486038
   20176122	안시성	5413370
   20184678	배반의 장미	29890
   20187521	펭귄 하이웨이	25631
   20180628	액슬	12152
   20180770	다이노 어드벤처2: 육해공 공룡 대백과	34822
   20189462	셜록 놈즈	83846
   20177308	협상	1953273
   20188661	에브리데이	21620
   20172204	명당	2066465
   20167903	원더풀 고스트	439910
   20189262	더 넌	1007366
   20185046	서치	2944333
   20188304	극장판 요괴워치 섀도사이드: 도깨비왕의 부활	151054
   20189268	루이스	89501
   20180167	에그엔젤 코코밍: 두근두근 핼러윈 파티	42980
   20189746	극장판 뽀잉: 슈퍼 변신의 비밀	35688
   20156554	물괴	702096
   20153446	너의 결혼식	2812226
   20188581	더 프레데터	169814
   20189362	업그레이드	178153
   20177537	상류사회	760945
   20181942	맘마미아!2	2280120
   20186202	신과함께-인과 연	12264813
   20179101	공작	4968325
   20170670	목격자	2512159
   20189261	어드리프트:우리가 함께한 바다	41977
   20187647	나를 차버린 스파이	258016
   20181181	미션 임파서블: 폴아웃	6567099
   20139221	그래비티	3262924
   20184802	몬스터 호텔 3	1023630
   20183584	메가로돈	515536
   20187657	마일22	51350
   20187641	극장판 도라에몽: 진구의 보물섬	138640
   20187427	명탐정 코난 : 제로의 집행인	377257
   20186501	극장판 헬로카봇 : 백악기 시대	854230
   20183361	인크레더블 2	2998015
   20185242	신비아파트: 금빛 도깨비와 비밀의 동굴	667879
   20186121	어느 가족	123887
   20170942	인랑	891308
   20180522	앤트맨과 와스프	5444801
   20185341	마녀	3188405

   

### 2.  영화 상세정보(영화진흥위원회 오픈 API)

1. 영화 상세정보에 필요한 데이터를 저장한다.

   *  `boxoffice.csv` 에 저장한 dictionary를 불러온다.

   * 불러온 data 중 movieCd의 value 값만 저장된 리스트를 만든다.

   ```PYTHON
   with open('boxoffice.csv', 'r', encoding='utf-8') as f:
       reader = csv.DictReader(f)
   
       for row in reader:
           movies.append(row['movieCd'])
   ```

   

2. 기본 요청 url을 이용하여 `영화 대표코드` , `영화명(국문)` , `영화명(영문)` , `영화명(원문)` , `관람등급` , `개봉년도` , `상영시간` , `장르` , `감독명` 을 뽑아낸다.

   * 기본요청 url :  http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.xml (또는 .json)

   * 인터페이스

     ![1563772798673](C:\Users\student\Desktop\과제\1563772798673.png)

   ```python
   for movieCd in movies:        
       api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'
       response = requests.get(api_url).json()     
   ```

3. 뽑아낸 data를 다시 새로운 dictionary에 저장한다.

   * 장르, 관람등급, 감독명이 없거나 다른 경우의 예외처리를 해준다.

   ```python
   movieTotalInfo[movieCd] = {
           'movieCd': informations['movieCd'],
           'movieNm': informations['movieNm'],
           'movieNmEn': informations['movieNmEn'],
           'movieNmOg': informations['movieNmOg'],
           'openDt': informations['openDt'],
           'showTm': informations['showTm'],
           'genreNm': informations['genres'][0]['genreNm'],
           'watchGradeNm': informations['audits'][0]['watchGradeNm'] if informations['audits'] else None,
           'peopleNm': informations['directors'][0]['peopleNm'] if informations['directors'] else None
           }
   ```

4. 필요한 data를 저장한 dictionary를 movie.csv파일로 저장한다.

   ```python
   with open('movie.csv', 'w', encoding='utf-8') as f:
       fieldnames = ['movieCd', 'movieNm', 'movieNmEn', 'movieNmOg', 'openDt','showTm', 'genreNm', 'watchGradeNm', 'peopleNm']
       csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
       csv_writer.writeheader()
       for item in movieTotalInfo.values():
           csv_writer.writerow(item)
   ```

5. **결과**

   다음과 같은 형태로 저장된다.

   **총 186개**
   
   ![1563773420311](C:\Users\student\Desktop\과제\1563773420311.png)



### 3. 영화인 정보 (영화진흥위원회 오픈 API)

1. 영화인 정보에 필요한 데이터를 저장한다.

   - `movie.csv` 에 저장한 dictionary를 불러온다.
   - 불러온 data 중 peopleNm의 value 값만 저장된 list를 만든다.

   ```PYTHON
   with open('movie.csv', 'r', encoding='utf-8') as f:
       reader = csv.DictReader(f)
       for row in reader:
           peoples.append(row['peopleNm'])
   ```

   

2. 기본 요청 url을 이용하여 `영화인 코드` , `영화인명` , `분야` , `필모리스트` 를 뽑아낸다.

   - 기본요청 url :  http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.xml (또는 .json)

   - 인터페이스

     ![1563773694093](C:\Users\student\Desktop\과제\1563773694093.png)

     ```python
     for peopleNm in peoples:        
         api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}&peopleNm={peopleNm}'
         response = requests.get(api_url).json()
     ```

3. 뽑아낸 data를 다시 새로운 dictionary에 저장한다.

   - `감독` 인 data와 필요한 내용이 있는 data만 뽑아내 새로운 dictionary를 만든다.

   ```python
   people_info = response['peopleListResult']['peopleList']
       if '감독' == people_info[0]['repRoleNm'] and peopleNm == people_info[0]['peopleNm']:
           peopleTotalInfo[peopleNm] = {
               'peopleNm': people_info[0]['peopleNm'] if people_info[0] else None,
               'peopleCd': people_info[0]['peopleCd'] if people_info[0] else None,
               'repRoleNm': people_info[0]['repRoleNm'] if people_info[0] else None,
               'filmoNames': people_info[0]['filmoNames'] if people_info[0] else None,
           }
   ```

4. 필요한 data를 저장한 dictionary를 director.csv파일로 저장한다.

   ```python
   with open('director.csv', 'w', encoding='utf-8') as f:
       fieldnames = ['peopleNm', 'peopleCd', 'repRoleNm', 'filmoNames']
       csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
       csv_writer.writeheader()
       for item in peopleTotalInfo.values():
           csv_writer.writerow(item)
   ```

5. **결과**

   다음과 같은 형태로 저장된다.

   **총 144명**

   ![1563841621399](C:\Users\student\Desktop\1563841621399.png)