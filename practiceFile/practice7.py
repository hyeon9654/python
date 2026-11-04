# Practice7 문제 [ 씨네21(Cine21) 영화 평점 및 핵심 정보 수집 ]
# 출처 및 대상: 씨네21 영화 평점 페이지,  https://cine21.com/movie/point

# 1. 동적페이지(씨네21 동적 페이지네이션) vs 정적페이지
# 2. 주소: https://cine21.com/movie/point
# 3. 제목, 이미지 링크, 전문가 평점 = list_with_upthumb_item
# p.title  , .img_wrap>img , .star_wrap > p.num
# 4. 클릭이벤트 : dom.click() ,  .pagination .page a 

# Practice7 문제 [ 씨네21(Cine21) 영화 평점 및 핵심 정보 수집 ]
# 출처 및 대상: 씨네21 영화 평점 페이지,  https://cine21.com/movie/point

# 1. 동적페이지(씨네21 동적 페이지네이션) vs 정적페이지
# 2. 주소: https://cine21.com/movie/point
# 3. 제목, 이미지 링크, 전문가 평점 = list_with_upthumb_item
# p.title  , .img_wrap>img , .star_wrap > p.num
# 전문가 평점은 '전문가'라고 표시된 .star_wrap 내부에서 추출
# 4. 클릭이벤트 : dom.click() ,  .pagination .page a
# 영화 평점 목록인 #point_list_holder 내부에서만 요소를 찾음
import asyncio
from playwright.async_api import async_playwright
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 1] 라이브러리 호출
import asyncio  # 비동기 라이브러리
from playwright.async_api import async_playwright   # 브라우저 자동화 라이브러리

# 2] Playwright의 비동기 기능을 사용하기 위한 함수 선언
async def 실습7() :
    # 3] 비동기 Playwright 실행 및 종료 관리
    async with async_playwright() as 비동기통신 :
        # 4] 크롬과 비슷한 백그라운드 실행 가능한 브라우저 프로그램
        브라우저 = await 비동기통신.chromium.launch( headless=False )  # False = 뷰모드 # True = 백그라운드
        # 5] 브라우저에 새탭/페이지 열기
        페이지 = await 브라우저.new_page()
        # 6] 열린 페이지에 원하는 홈페이지 주소로 이동
        await 페이지.goto( "https://cine21.com/movie/point" )
        await 페이지.wait_for_timeout( 5000 )   # 밀리초 만큼 일시정지 / 5초

        # 실제 영화 평점 목록이 나타날 때까지 기다림
        await 페이지.locator(
            '#point_list_holder .list_with_upthumb_item'
        ).first.wait_for( state='visible' )

        영화리스트 = []

        # ====================================================================================== #
        for i in range( 1, 4 ) :                         # 1부터 3까지 반복
            # 7] query_selector_all(식별자) : 여러 개 DOM 반환, query_selector(식별자) : 한 개 DOM 반환
            # 여기서는 페이지 갱신 후에도 요소를 다시 찾는 locator를 사용
            페이지버튼리스트 = 페이지.locator( '#point_list_holder .pagination .page a' )

            # 8] 반복문 이용하여 버튼 하나씩 클릭 .click()
            # 1페이지는 처음 접속했을 때 표시되므로 2페이지부터 해당 번호를 클릭
            if i > 1 :
                # 영화 목록을 가져오는 응답을 기다림
                async with 페이지.expect_response(
                    "https://cine21.com/movie/point/list_items"
                ) as 응답정보 :
                    await 페이지버튼리스트.get_by_text( str( i ), exact=True ).click()

                응답 = await 응답정보.value
                await 응답.finished()

                # 응답을 받은 뒤 화면에도 해당 페이지 번호가 반영됐는지 확인
                await 페이지.wait_for_function(
                    """번호 => {
                        const 버튼 = document.querySelector(
                            '#point_list_holder .pagination .page a.on'
                        );
                        return 버튼 && 버튼.textContent.trim() === String(번호);
                    }""",
                    arg=i
                )

            # 9] 영화 카드에서 제목, 이미지 링크, 전문가 평점 추출
            items = 페이지.locator( '#point_list_holder .list_with_upthumb_item' )

            for j in range( await items.count() ) :
                item = items.nth( j )

                # p.title  , .img_wrap>img , .star_wrap > p.num
                영화제목 = item.locator( 'p.title' )
                영화제목 = await 영화제목.inner_text() if await 영화제목.count() > 0 else "제목없음"

                이미지링크 = item.locator( '.img_wrap>img' )
                이미지링크 = await 이미지링크.get_attribute( 'src' ) if await 이미지링크.count() > 0 else "이미지없음"

                # 관객 평점과 구분하여 전문가 평점만 선택
                전문가평점 = item.locator( '.star_wrap' ).filter(
                    has_text='전문가'
                ).locator( 'p.num' )
                전문가평점 = await 전문가평점.inner_text() if await 전문가평점.count() > 0 else "전문가평점없음"

                # 수집한 데이터를 딕셔너리로 묶어 리스트에 저장
                영화정보 = {
                    '영화제목': 영화제목,
                    '이미지링크': 이미지링크,
                    '전문가평점': 전문가평점
                }
                영화리스트.append( 영화정보 )

        # 모든 페이지 수집 후 최종 출력
        print( 영화리스트 )

        # 브라우저 종료
        await 브라우저.close()

asyncio.run( 실습7() )

# [1. 목표]
# Playwright의 비동기 제어와 동적 페이지네이션(click)을 활용해 여러 페이지를 순회한다.
# 영화 아이템 카드에서 제목, 이미지 링크, 전문가 평점 3가지 핵심 데이터를 정확히 추출하여 구조화한다.

# [2. 데이터 수집 요구사항]
# 2-1 (페이지 순회): 1페이지부터 3페이지까지 반복문을 통해 동적으로 페이지를 이동한다.
# 2-2 (요소 추출): 각 영화 카드 내부에서 아래 3가지 요소를 각각 수집한다.
# 영화 제목 # 이미지 # 전문가 평점

# 2-3 (데이터 적재): 수집된 데이터를 딕셔너리로 묶어 리스트에 저장하고 최종 출력한다.

# [1. 목표]
# Playwright의 비동기 제어와 동적 페이지네이션(click)을 활용해 여러 페이지를 순회한다.
# 영화 아이템 카드에서 제목, 이미지 링크, 전문가 평점 3가지 핵심 데이터를 정확히 추출하여 구조화한다.

# [2. 데이터 수집 요구사항]
# 2-1 (페이지 순회): 1페이지부터 3페이지까지 반복문을 통해 동적으로 페이지를 이동한다.
# 2-2 (요소 추출): 각 영화 카드 내부에서 아래 3가지 요소를 각각 수집한다.
# 영화 제목 # 이미지 # 전문가 평점

# 2-3 (데이터 적재): 수집된 데이터를 딕셔너리로 묶어 리스트에 저장하고 최종 출력한다.