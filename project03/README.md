# Project03

## 03 - Web(HTML/CSS를 활용한 웹 사이트 구성)

* 영화 추천 사이트 메인 레이아웃을 구축합니다.

1. layout.css

   1. **HTML 기초**

      * `header` : 상단에 고정시키며 우선하여 볼 수 있도록 고정시킨다.

        ```css
        header {
          position: sticky; /* 화면을 조정해도 정해진 위치에 고정 */
            /* fixed도 사용가능 */
          top: 0; /* 상단에 위치시킨다 */
          z-index: 100; /* 제일 앞쪽에 위치하게 하는것*/
        }
        ```

      * `nav` 및 `nav-items > li`  : 네비게이션 항목을 오른쪽으로 정렬후 한줄로 만든다. 

        ​												(좌우 여백과 bullet point 제거 및 링크 형태 변형)

        ```css
        nav {
          float: right;   /* navigation 항목을 오른쪽으로 정렬 */
        }
        
        .nav-items > li {
          display: inline-block; /* navigation 항목을 한 줄로 만들어 준다. */
          margin: 0 8px; /* 좌우 여백 */
          list-style: none; /* li 태그의 bullet point를 제거 */
        }
        
        .nav-items > li > a {
          color: #666;
        }
        
        .nav-items > li > a:hover { /* hover는 마우스 오버시 모습 */
          color: #e36; /* 이때 하이라이트 되도록 다른 색상 변경 */
          text-decoration: none; /* 밑줄 제거 */
        }
        ```

      * `title section` : 배경이미지 적용 및 텍스트 설정

        ```css
        #section-title {
          background-image: url(images/background.jpg);/* 이미지 적용 */
          text-align: center; /* 텍스트를 가운데 정렬 */
          /* 텍스트를 수직 가운데 정렬. */
          line-height: 320px; /* 정렬을 위한 높이 지정 */
          vertical-align: middle;
        }
        
        .section-title-heading {
          font-size: 3em;
        }
        ```

      * `aside` : aside의 위치 지정 및 패딩, 불 포인드 제거

        ```css
        aside {
          position: absolute;
          left: 0;
        }
        
        .aside-items {
          -webkit-padding-start: 0px;  /* ul 태그의 자동으로 적용된 padding을 제거 */
        }
        
        .aside-items > li {
          list-style: none; /* li 태그의 bullet point를 제거 */
        }
        ```

      * `footer` : 하단에 위치하도록  position 설정 및 텍스트 설정

        ```css
        footer {
          position: fixed; /* footer는 항상 바닥에 위치하도록 설정 */
          bottom: 0;
          text-align: center;
          line-height: 50px;
          vertical-align: middle;
        }
        ```

   2. 실행 화면

      ![](C:\Users\student\Desktop\Jimin\web\project\project03\결과물.JPG)

