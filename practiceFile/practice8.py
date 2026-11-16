# Practice8: API 데이터 수집
# 1. 개요 및 대상 API 정보
# API 이름: 행정안전부_착한가격업소 현황
# API URL: https://www.data.go.kr/data/3045247/fileData.do 

# 목표: httpx를 통해 공공데이터 API를 호출하고, pandas를 활용해 업소명, 주소, 가격 데이터를 구조화한 뒤 통계 분석을 수행합니다.
# 2. 상세 요구사항
# 2-1 (API 호출 및 파라미터 설정):
# 지정된 API URL에 인증키(serviceKey)를 포함하여 요청합니다.
# 임의의 100건의 데이터를 수집
import httpx
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
api_url = 'https://api.odcloud.kr/api/15172358/v1/uddi:d45599dd-2090-4bbb-abde-dbe9f9c6e75a'
serviceKey = '여기에_본인의_일반_인증키_입력'

params = {'page': 1, 'perPage': 100, 'serviceKey': serviceKey}

response = httpx.get(api_url, params=params, timeout=30.0)
response.raise_for_status()
result = response.json()

# 2-2 (데이터프레임 적재):
# 응답받은 JSON 데이터 중 실제 행 목록인 data 배열을 추출하여 pandas.DataFrame으로 변환합니다.
if 'data' not in result:
    raise ValueError(f'API 응답 확인 필요: {result}')

df = pd.DataFrame(result['data'])
df = df.rename(columns={'업종1(대분류)': '업종', '착한가격메뉴 가격1': '가격1'})

print('수집 건수:', len(df))
print(df[['업소명', '주소', '업종', '가격1']].head())

# 2-3 (데이터 전처리 및 분석):
# 가격1 컬럼의 데이터를 숫자형(pd.to_numeric)으로 변환합니다.
df['가격1'] = pd.to_numeric(df['가격1'].astype(str).str.replace(',', '', regex=False), errors='coerce')

# 수집된 100건 데이터 기준 가격1의 평균값을 산출하여 출력합니다.
print('가격1 평균:', df['가격1'].mean())

# 2-4 (업종별 평균 가격 집계 및 시각화):
# groupby('업종')을 사용하여 업종별 가격1의 평균 가격을 계산합니다.
group_mean = df.groupby('업종')['가격1'].mean().reset_index()
print(group_mean)

# seaborn의 barplot 활용하여 업종별 평균 가격 비교 막대그래프를 시각화합니다.
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

sns.barplot(data=group_mean, x='업종', y='가격1')
plt.title('착한가격업소 업종별 평균 가격')
plt.xlabel('업종')
plt.ylabel('평균 가격(원)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()