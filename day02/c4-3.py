# p.231
# 범위 함수 : range( )
# 1. range( 수 )
print( range(5) ) # range( 0,5 )
print( list(range(5)) ) # [0, 1, 2, 3, 4]

# 2. range( 시작값, 끝값 )  # range(2,10)   -> 2 ~ 9
print(list(range( 3, 6 ))) # [ 3,4,5 ]

# 3. range( 시작값, 끝값, 단계 )
print(list(range( 0, 10, 2 )))  # 0부터 9까지 2씩증가

# p.233
# for 과 range 함수 함께, for 반복변수 in range
# 1] 1부터 10까지 출력
for i in range( 1,11 ):
    print( i )
# 2] 10부터 1까지 출력
for i in range( 10, 0 , -1 ):
    print(i)
# 3] 1부터 10까지 홀수만 출력
for i in range( 1, 11, 2 ):
    print( i )
# 4] 구구단 : 단수 2부터 9까지, 곱수 1부터 9까지
for i in range(2,10,1):
    for j in range(1,10,1):
        print( f"{i} x {j} =  {i * j}" )

# p.240
# while 조건식 :    # 조건이 True이면 실행코드 반복실행, False 반복종료
#       실행코드
# 예1] 1부터 10까지 출력
i = 0
while i < 11:
    print( i )
    i += 1  # 파이썬 증감식연산자 X

# 예2] while 과 리스트
list_a = [ 1,2,1,2 ]
value = 2
while value in list_a:  # 찾을 값 in 리스트명,
    # 리스트내 2가 존재하면 반복실행
    list_a.remove( value )
print( list_a ) # [ 1, 1 ]

# p.244 break, continue 키워드 : 반복문에서 사용하는 키워드
for i in range( 1,11,1 ):
    if i == 3:
        break
    print( i )

for i in range( 1, 11, 1 ):
    if i == 3:
        continue
    print( i )