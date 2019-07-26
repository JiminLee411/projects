# Project02

## 파이썬을 활용한 데이터 수집 2

* 영화평점서비스를 만들기 위한 데이터 수집을 위해 영화 데이터베이스 구축을 위한 csv파일을 만듭니다.

1. **네이버 영화 검색 API - `movie_naver.py`**

   * **Project01**에서 얻은 영화명(국문) 을 바탕으로 `네이버 영화 검색 API`를 통해 추가적인 데이터를 수집합니다.  *(해당 데이터는 향후 영화평점서비스에서 기준 평점 및 영화 포스터 썸네일로 활용될 것입니다.)*

     * [네이버 영화 검색 API](https://developers.naver.com/docs/search/movie/) 를 통해 API 등록 (등록시 사용 API에 `검색` 추가!)

     

     1. 네이버 API 설정

        1. .env` 파일에 `NAVER_CLIENT_ID` 와  `NAVER_CLIENT_SECRET` 를 선언한다.

           - `python_decouple` 을 이용할 때, 환경변수 파일로 관리한다는 것

             

        2. `.gitignore` 파일을 만든후 `.env` 파일을 넣어준다.

           

        3. `movie_naver.py` 파일에 네이버 API를 설정한다.

           ```python
           client_id = config('NAVER_CLIENT_ID')
           client_secret = config('NAVER_CLIENT_SECRET')
           ```

           

     2. 헤더 설정

        1.  요청시 필요한 id와 secret을 위해 `movie_naver.py` 파일에 헤더를 설정해준다.

           ```python
           headers = {
               'X-Naver-Client-Id': client_id,
               'X-Naver-Client-Secret': client_secret
           }
           ```

           

     3. 변수 선언

        ```python
        import requests
        from decouple import config
        import csv
        
        movie_names = [] # 영화명(국문) str 저장할 빈 list 선언
        movie_codes = [] # 영화 대표코드 str 저장할 빈 list 선언
        naver_movie_info = {} # 최종 데이터들(영화 대표코드, 하이퍼텍스트 link, 썸네일 이미지의  URL, 유저 평점)을 저장할 dictionary 선언
        
        # 요청할 api_url 정의
        api_url = 'https://openapi.naver.com/v1/search/movie.json'
        ```

        

     4. `movie.csv` 불러오기

        ```python
        # movie.csv를 f 변수에 utf-8로 읽는다.
        with open('movie.csv', 'r', encoding='utf-8') as f: 
            reader = csv.DictReader(f)
            
            # 필요한 데이터(영화명(국문), 영화 대표코드)를 각각의 리스트에 저장한다.
            for row in reader:
                movie_names.append(row['movieNm'])
                movie_codes.append(row['movieCd'])
        ```

        

     5. 요청/응답 및 딕셔너리에 저장하기

        ```python
        # zip()을 이용하여 같은 영화명과 영화대표코드를 묶어서 빼내는 방식을 이용하였다.
        for query, movieCd in zip(movie_names, movie_codes):
            
            # 응답을 .json()으로 response에 저장
            response = requests.get(f'{api_url}?query={query}', headers=headers).json()
            information = response['items'][0]
            
            # dictionary에 네이버 영화 정보 저장
            naver_movie_info[movieCd] = {
                
                # key인 'items'의 value값은 list이므로 예외처리를 해준다.
                '영화 대표코드': movieCd,
                '링크': information['link'] if response['items'] else None,
                '이미지URL': information['image'] if response['items'] else None,
                '유저 평점': information['userRating'] if response['items'] else None
                
            }
        ```

        

     6. 저장한 dictionary를 `.csv` 파일로 저장한다.

        ```python
        # movie_naver.csv에 생성한 dictionary를 utf-8로 저장한다.
        with open('movie_naver.csv', 'w', encoding='utf-8') as f:
            fieldnames = ['영화 대표코드', '링크', '이미지URL', '유저 평점']
            csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
            csv_writer.writeheader()
            
            for item in naver_movie_info.values():
                csv_writer.writerow(item)
        ```

        

   

2. **영화 포스터 이미지 저장 - `movie_image.py`**

   * 앞서 네이버 영화 검색 API를 통해 얻은 이미지 URL에 요청을 보내 실제 이미지 파일로 저장합니다.

   

   1. 변수 선언

      ```python
      import requests
      import csv
      
      # 변수 선언
      movie_img_url = [] # 썸네일 이미지의  URL str 저장할 빈 list 선언
      movie_codes = [] # 영화 대표코드 str 저장할 빈 list 선언
      ```

      

   2. `movie_naver.csv` 불러오기

      ```python
      with open('movie_naver.csv', 'r', encoding='utf-8') as f:
          reader = csv.DictReader(f)
          for row in reader:
              movie_img_url.append(row['이미지URL']) # 인터넷 상의 이미지파일을 list에 저장
              movie_codes.append(row['영화 대표코드']) 
      ```

   3. 요청 및 파일 저장

      ```python
      for url, movieCd in zip(movie_img_url, movie_codes):
          with open(f'images/{movieCd}.jpg', 'wb') as f: # wb : 바이너리 파일을 쓰겠다.
              response = requests.get(url)
              f.write(response.content) # 텍스트형식(json, html, xml....)이 아닌 형식을 받을 때는 .content
      ```

      



















