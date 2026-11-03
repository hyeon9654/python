# httpx란? 외부 api 통신하는 라이브러리, API연동 / SPRING API
# 설치1 : pip install https
# httpx 라이브러리에는 .json() 타입변환 하지만 xml변환 지원하지 않는다.
# xmltidict란? xml 파싱 라이브러리
# 설치2 : pip install xmltodict

import httpx
import pandas as pd

# 0] 공공데이터포털 본인 인증기
service_key = "7540ef37d4d62e8aa1ccaf9c61bc9095638232be0930450a4a0d128c78e9e7d6"

# 1] 공공데이터에 json 형식의 자료요청
def test1() :
    # https://api.odcloud.kr/api/15052602/v1/uddi:855807e2-fe8a-4e47-8a5a-ce1894e410d7_201909031553?page=1&perPage=10&serviceKey=7540ef37d4d62e8aa1ccaf9c61bc9095638232be0930450a4a0d128c78e9e7d6
    # 2] 신청한 API의 주소및 파라미터 분석, page 현재페이지, perPage=페이지당자료수, serviceKey
    url = "https://api.odcloud.kr/api/15052602/v1/uddi:855807e2-fe8a-4e47-8a5a-ce1894e410d7_201909031553"
    url += "?Page=1"
    url += "&perPage=147"
    url += f"&ServiceKey={service_key}"
    # 3] httpx 이용하여 통신하기, import httpx
    # httpx.HTTP메소드명(통신할 주소), 통신 결과 반환
    response = httpx.get( url )
    print( response )   # < Response [200 OK] > 성공 했다는 뜻
    # 4] 응답결과 JSON 변환 , .json()
    response_json = response.json()     # print( response_json )
    # 5] 판다스에 저장하기, import pandas as pd
    df = pd.DataFrame(response_json['data'])
    df.info()
test1()

# 2] 공공데이터포털 xml 형식의 자료 요청, 국립중앙의료원_전국 약국 정보 조회
import xmltodict    # sml 변환 라이브러리
def test2() :
    # 1] 요청할 API 주소
    url = "https://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown"
    url += f'?ServiceKey={service_key}'
    url += 'pageNo=1&numOfRows=100'

    # 2] httpx 이용한 api 요청
    response = httpx.get( url )
    # 3] 요청 응답 자료를 문자열로 반환하여 파이썬 dict 형식으로 변환
    response_dict = xmltodict.parse( response.text )    # print(response_dict)
    # 4] <response> -> <body> -> <items> -> <item>
    df = pd.DataFrame( response_dict['response']['body']['items']['item'] )
    df.info()
test2()
