# 293 재귀함수, 재귀란? 자기 자신을 호출하는 것
# 1] 팩토리얼
def factorial1(n):
    output = 1
    for i in range( 1, n+1 ):
        output *= i
    return output
factorial1(2)   # 2! -> 1*2
factorial1(3)   # 3! -> 1*2*3
# 만약에 n이 3이면 range( 1, 4 ) 반복하므로
# i는 1일때 ouput = output * 1
# i는 2일때 ouput = output * 2
# i는 3일때 ouput = output * 3
# 1 * 2 * 3 => 3!

# 2] 팩토리얼 재귀
def factorial2(n):
    # 무한 재귀 방지
    if n == 0:
        return 1
    else:   # 재귀함수                  ↑↓→
        return n * factorial2(n-1)
factorial1(2)   
factorial1(3)   

# 구구단 반복문
for 단 in range( 2,10,1 ):          # 단 : 2부터 9까지 1씩증가
    for 곱 in range( 1, 10, 1 ):    # 곱 : 1부터 9까지 1씩증가
        print(단*곱)
# 3단까지의 반복문 순서도 작성

# 구구단 재귀함수
def 구구단( 단 = 2, 곱 = 1 ):
    if 단 > 9 : # 재귀 끝
        return
    if 곱 > 9 : # 곱하기 9까지 했으면 단 올리기
        구구단( 단 + 1 , 1 )
        return
    print(단*곱)
    구구단(단,곱+1) # 곱올리기
구구단()

# 297p. 피보나치수열1  -------------------
counter = 0 
def fibonacci( n ) : 
    print( "fibonacci({})를 구합니다".format(n) )
    global counter
    counter += 1 
    if n == 1 :
        return 1 
    if n == 2 : 
        return 1 
    else : 
        return fibonacci( n-1 ) + fibonacci( n - 2 )
print( fibonacci( 5 ) ) 

# 301p. 피보나치수열2 메모화 -------------
dictionary = { 1 : 1 , 2 : 1 }
def fibonacci2( n ) : 
    if n in dictionary :
        return dictionary[n]
    else : 
        output = fibonacci2( n - 1 ) + fibonacci2( n - 2 )
        dictionary[n] = output
        return output
print( fibonacci2( 5 ) ) 

# 문제풀이
테이블최솟값=2
테이블최댓값=10
전체인원=100
memo={}

def 문제(남은사람수,최소사람수):
    key = str([남은사람수,최소사람수])

    # 종료 조건
    if key in memo:
        
    if 남은사람수 < 0:
        
    if 남은사람수 == 0:
       

    # 재귀 처리

    # 메모화 처리

    # 종료

print(문제(전체인원,테이블최솟값))