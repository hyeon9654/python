# PythonML Practice 2: 다항 규제 회귀 기반 성적 예측
# 데이터 출처: https://www.kaggle.com/datasets/shambhurajejagadale/student-performance-prediction-dataset
# 1. 데이터 준비 및 전처리
#  - Kaggle 데이터셋을 불러옵니다.
import pandas as pd
df = pd.read_csv('./Student_Performance.csv')
#  - 범주형 변수를 제외한 6개 수치형 컬럼을 독립변수(X, 문제지)로 추출하세요:
X = df[['study_hours', 'attendance', 'sleep_hours', 'internet_usage', 'assignments_completed', 'previous_score']]
#  - 시험 성적인 'exam_score' 컬럼을 종속변수(Y, 정답지)로 설정하세요.
Y = df['exam_score']

# 2. 데이터 분할
#  - train_test_split을 사용하여 훈련 세트(80%)와 테스트 세트(20%)로 분할하세요.
from sklearn.model_selection import train_test_split
#  - 재현성을 위해 random_state=42로 고정합니다.
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=0.2, random_state=42 )

# 3. 다항 특성 확장 및 표준화 (고정 차수: degree=2)
#  - PolynomialFeatures(degree=2, include_bias=False)를 사용하여 2차 다항 특성을 생성하세요.
from sklearn.preprocessing import PolynomialFeatures
#    * 훈련 세트(X_train)로만 .fit()을 수행하고, X_train과 X_test를 각각 .transform() 하세요.
poly = PolynomialFeatures(degree=2, include_bias=False)
poly.fit(X_train)
X_train_poly = poly.transform(X_train)
X_test_poly = poly.transform(X_test)
print(X_train_poly.shape)
print(X_test_poly.shape)
#  - StandardScaler를 생성하고, 다항 확장된 훈련 세트(X_train_poly) 기준으로 .fit()한 뒤 표준 점수로 변환하세요.
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
#    * 특성 간 스케일 차이를 맞추기 위해 훈련 세트와 테스트 세트 모두 .transform() 하세요.
ss.fit(X_train_poly)
X_train_scaled = ss.transform(X_train_poly)
X_test_scaled = ss.transform(X_test_poly)
print(X_test_poly[0])
print(X_train_scaled[0])

# 4. 3가지 모델 학습 및 결정계수(R²) 비교 (고정 규제: alpha=1.0)
from sklearn.linear_model import LinearRegression, Ridge, Lasso
linear = LinearRegression()
linear.fit(X_train_scaled,Y_train)

ridge = Ridge(alpha=1.0, random_state=42)
ridge.fit(X_train_scaled,Y_train)

lasso = Lasso(alpha=1.0, random_state=42)
lasso.fit(X_train_scaled,Y_train)

#  - 3가지 회귀 모델을 각각 생성하고 스케일링된 훈련 데이터로 학습시키세요:
#    1) LinearRegression()
#    2) Ridge(alpha=1.0, random_state=42)
#    3) Lasso(alpha=1.0, random_state=42)
#  - 각 모델별 훈련 세트 R² 점수(Train R²)와 테스트 세트 R² 점수(Test R²)를 각각 산출하여 비교 출력하세요.
print(": --------------------- LinearRegression ---------------------")
print( "Train R2: ", linear.score( X_train_scaled, Y_train ) )
print( "Test R2: ", linear.score( X_test_scaled, Y_test ) )
print(": --------------------- Ridge ---------------------")
print( "Train R2: ", ridge.score( X_train_scaled, Y_train ) )
print( "Test R2: ", ridge.score( X_test_scaled, Y_test ) )
print(": --------------------- Lasso ---------------------")
print( "Train R2: ", lasso.score( X_train_scaled, Y_train ) )
print( "Test R2: ", lasso.score( X_test_scaled, Y_test ) )     


# 5. 임의 대조군 데이터에 대한 3가지 모델 예측 비교
#  - 아래 대조군 샘플 2개를 준비하세요:
#    * 샘플 1 (상위권): study_hours=9, attendance=95, sleep_hours=7, internet_usage=2, assignments_completed=18, previous_score=85
#    * 샘플 2 (하위권): study_hours=2, attendance=60, sleep_hours=5, internet_usage=9, assignments_completed=4, previous_score=50
#  - 각 샘플 데이터를 앞서 학습시킨 동일한 변환기(PolynomialFeatures, StandardScaler)로 변환하세요.
#  - 3가지 모델(LinearRegression, Ridge, Lasso)에 변환된 데이터를 각각 대입하여 예상 시험 성적을 산출하고 비교 출력하세요.
SampleData1 = pd.DataFrame([[9,95,7,2,18,85]], columns=X.columns)
SampleData2 = pd.DataFrame([[2,60,5,9,4,50]],columns=X.columns)

SampleData1_poly = poly.transform(SampleData1)
SampleData2_poly = poly.transform(SampleData2)

SampleData1_scaled = ss.transform(SampleData1_poly)
SampleData2_scaled = ss.transform(SampleData2_poly)

print(": --------------------- LinearRegression ---------------------")
print( "샘플1 예상 성적: ", linear.predict( SampleData1_scaled )[0] )
print( "샘플2 예상 성적: ", linear.predict( SampleData2_scaled )[0] )
print(": --------------------- Ridge ---------------------")
print( "샘플1 예상 성적: ", ridge.predict( SampleData1_scaled )[0] )
print( "샘플2 예상 성적: ", ridge.predict( SampleData2_scaled )[0] )
print(": --------------------- Lasso ---------------------")
print( "샘플1 예상 성적: ", lasso.predict( SampleData1_scaled )[0] )
print( "샘플2 예상 성적: ", lasso.predict( SampleData2_scaled )[0] )   