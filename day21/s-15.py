import torch # 파이토치 라이브러리 호출
# 1. cpu/gpu 확인 가능
device = 'cuda' if torch.cuda.is_available() else 'cpu' # cuda : GPU 장치
print( device ) # cpu # 런타임 유형 변경가능
# 2. 파이토치는 텐서(tensor) 객체
import numpy as np
np_data = np.array( [ [10.0, 20.0, 30.0], [40.0, 50.0, 60.0] ] )
# x = torch.tensor( 넘파이배열, dtype=torch.타입명 )
x = torch.tensor( np_data, dtype=torch.float32 )
print( x.shape , x.dtype ) # 차원확인(2,3), 타입 확인
# 3. 차원 재구성
print( x.reshape( 3, 2 ).shape ) # torch.Size([3, 2])  # 차원변경
print( x.unsqueeze(0).shape ) # torch.Size([1, 2, 3])  # x.unsqueeze(차원위치)
print( x.unsqueeze(-1).shape ) # torch.Size([2, 3, 1]) # 차원추가
# 4. 차원 변경시 기존 자료들을 1차원으로 펼친 다음에 해당 차원으로 재구성
print( x ) # [ [10., 20., 30.],[40., 50., 60.] ] # (2,3)
x2 = x.reshape(3,2)
print( x2 ) # [  [10., 20.]  ,  [30., 40.]  ,  [50., 60.]  ] # (3,2)
x3 = x.unsqueeze(1)
print( x3 ) # [ [  [10., 20., 30.] ] , [ [40., 50., 60.]]  ]  # (2,1,3)

import torch
sample=torch.tensor( [ -2.0 , 0.0 , 3.0 ] )
print( sample )
# 1. 시그모이드함수: 0~1 사이의 확률값으로 변환하는 함수
# ( 1 / ( 1 + e^-z) )
print( torch.sigmoid( sample ) ) # tensor([0.1192, 0.5000, 0.9526])
# 2. ReLU 활성화함수: 음수는 0으로 차단하고 양수만 표현
# max( 0 , z )
print( torch.relu( sample ) )    # tensor([0., 0., 3.])

import torch
x = torch.tensor( 2.0 ) # 특성값
y = torch.tensor( 1.0 ) # 타깃값
w = torch.tensor( 0.2, requires_grad=True ) # 가중치
# requires_grad=True 속성은 기울기 기록
b = torch.tensor( 0.0, requires_grad=True ) # 편향
learning_rate = 0.1
y_pred = x * w + b # y_pred = wx + b # 가중치 계산->예측
print( y_pred ) # 0.4
y_pred = torch.relu( y_pred ) # 활성화함수 => 통과/비통과 구분
print( y_pred )

import torch.nn as nn
criterion = nn.MSELoss()  # 손실 함수( 오차 구해주는 함수 )
loss = criterion( y_pred , y ) # 손실 구하기
print( loss ) # 0.3600 # y_pred = 0.4 y = 1 , 오차 = 0.6 # 제곱 오차

# 역전파
loss.backward()
print( w.grad.item() , b.grad.item() )
# -2.4000000953674316      -1.2000000476837158
# 가중치 기울기 : -2.4     편향 기울기 : -1.2

# 가중치 계산: 2 * x * (예측값 - 정답) =>  -2.4
# 2 * 2 * (0.4 - 1.0 ) => -2.4

# 편향 계산: 2  * (예측값 - 정답) =>  -2.4
# 2 * ( 0.4 - 1.0 ) => -1.2

# * 가중치 올리면 오차는 줄어드는가?  편향은 내리면 오차는 줄어드는가?

# 기울기 이용하여 가중치/편향 수정-> 1학습
with torch.no_grad() : # 기울기 기록을 일시 중지 블록 선언
  # 가중치업데이트( 경사하강법 ) : 가중치 = 기존가중치 - ( 학습률 * 기울기 )
  w -= learning_rate * w.grad # 0.2 - ( 0.1 * -2.4 ) => 0.44
  b -= learning_rate * b.grad # 0 - ( 0.1 * -1.2 ) => 0.12
  # 가중치/편향 기울기 0으로 초기화 ( 다시 계산 하기 위한 )
  w.grad.zero_()
  b.grad.zero_()
print( '한번 업데이트 이후:' , w , b ) # 가중치 , 편향 확인
print( w * x + b ) # 업데이트 이후 예측값