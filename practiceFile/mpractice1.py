# Practice1
# 1. 데이터 준비
#  - Seaborn 내장 데이터셋인 'tips'를 불러옵니다.
import seaborn as sns
import pandas as pd

df = sns.load_dataset('tips')
print(df.head())
#  - 독립변수(X, 문제지): 식사 총액 'total_bill' 컬럼 (2차원)
X = df[['total_bill']]
#  - 종속변수(Y, 정답지): 팁 'tip' 컬럼 (1차원)
Y = df['tip']
print(X.shape)
print(Y.shape)
# 2. 데이터 분할
#  - train_test_split을 사용하여 훈련 세트(80%)와 테스트 세트(20%)로 분할하세요.
from sklearn.model_selection import train_test_split
#  - 재현성을 위해 random_state=42로 고정합니다.
X_train,X_test,Y_train,Y_test = train_test_split( X, Y, test_size=0.2, random_state=42 )

# 3. 모델 학습 및 수학적 파라미터 확인 
#  - Scikit-learn의 LinearRegression 모델을 생성하고 훈련 데이터로 학습시킵니다.
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit( X_train, Y_train )
#  - 학습 완료 후 모델이 도출한 '기울기'와 'y절편'을 출력하세요.
print("기울기: ", model.coef_ )            # [[0.10696371]]
print("y절편: ", model.intercept_ )       # [0.92523556]

# 4. 성능 평가 및 신규 데이터 예측
#  - 테스트 세트(X_test)에 대한 예측값(Y_pred)을 생성하세요.
Y_pred = model.predict( X_test )
import numpy as np
#  - 실제값(Y_test)과 예측값(Y_pred)을 비교하여 R²(결정계수)와 RMSE(평균 제곱근 오차)를 산출하고 소수점 둘째 자리까지 출력하세요.
from sklearn.metrics import mean_squared_error, r2_score

r2 = r2_score(Y_test, Y_pred)
rmse = np.sqrt( mean_squared_error(Y_test, Y_pred ) )
print(f"R2: {r2:.2f}")
print(f"RMSE: {rmse:.2f}" )
#  - 만약 식사 총액이 $30, $100인 새로운 손님이 방문했을 때, 예상되는 팁 금액을 각각 예측하여 출력하세요.
new_X = pd.DataFrame({'total_bill': [30,100]})
new_pred = model.predict(new_X)

print(f"식사 총액 $30 -> 예상 팁 ${new_pred[0]:.2f}")
print(f"식사 총액 $100 -> 예상 팁 ${new_pred[1]:.2f}")

# 5. 결과 시각화 및 한계점 분석 
#  - Matplotlib을 활용하여 아래 3가지 요소를 하나의 차트에 시각화하세요:
import matplotlib.pyplot as plt 

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

sns.set_theme(font='Malgun Gothic', rc={'axes.unicode_minus': False}, style='whitegrid')
#  1. 테스트 세트의 실제 데이터 산점도 (X_test vs Y_test)
plt.scatter(X_test,Y_test,label='테스트 데이터')
#  2. 식사비 $5부터 $100까지 모델이 예측한 선형 회귀선
line_X = pd.DataFrame({'total_bill': [5,100]})
plt.plot(line_X['total_bill'], model.predict(line_X),color='blue', label="예측 회귀선")
#  3. 식사비 $50일 때의 모델 예측 지점 (붉은 점으로 강조)
point_X = pd.DataFrame({'total_bill': [50]})
plt.scatter(point_X['total_bill'], model.predict(point_X),color='red',s=80, label="$50 예상팁")

plt.xlabel('식사 총액($)')
plt.ylabel('팁 ($)')
plt.title('식사 총액에 따른 팁 예측')
plt.legend()
plt.show()
