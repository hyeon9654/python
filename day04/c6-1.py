# 구문 오류 : 실행 전 오류 , 실행 자체 불가능
# 런타임 오류 : 실행 중 오류, 예외
# 예외 처리 : 예외를 해결한는 모든 것을

# 조건문 또는 try
# 예1] 조건문 예외
input_a = input("정수입력:")
# int( ) 정수로 변환 함수
# int( input_a ) # ValueError
if input_a.isdigit() :  # 문자열.isdigit() : 문자열타입의 값이 숫자면 true
    int( input_a )
else:
    print("정수가 아닙니다.")

# 예2] try 예외
try :
    int( input_a ) # 예외가 발생할 것 같은 코드 
except : 
    print("정수가 아닙니다.")

# 예3] pass 키워드 , 예외 어떻게 처리할지 모른경우 일단 넘어가기 
try : 
    int( input_a )
except :
    pass

# 예4] else , 예외가 발생하지 않았을 떄
try :   # 예외가 발생할 가능성이 있는 코드 
    int( input_a )
except :# 예외가 발생했을 떄 실행코드 
    print( "정수가 아닙니다.")
else : # 예외가 발생하지 않았을 떄 실행코드
    print( "정수가 맞습니다.")

# 예5] finally , 예외가 발생하든 발생하지 않든 무조건 실행 코드 
try : 
    int( input_a )
except :
    print( "정수가 아닙니다.")
else : 
    print( "정수가 맞습니다.")
finally : # 무조건 실행되는 코드
    print( "코드가 끝났습니다.")

# 예6] finally 활용예
try:
    file = open("info.txt", "w")
    # open( 파일명 , 옵션 ) 파일불러오기 함수   # w옵션: 파일이 없으면 생성
    예외.발생해라() # 일부러 예외 발생!!!******
    # try에서 만약에 예외가 발생하면 발생한 코드 이후는 실행안됨 -> except
    # file.close()
    # 파일.close() : 파일닫기
except:
    print("예외가 발생했습니다.")
finally:
    file.close() # 파일.close(): 파일닫기


try:
    file = open("info.txt", "w")
    # open( 파일명 , 옵션 ) 파일불러오기 함수   # w옵션: 파일이 없으면 생성
    예외.발생해라() # 일부러 예외 발생!!!******
    # try에서 만약에 예외가 발생하면 발생한 코드 이후는 실행안됨 -> except
    # file.close()
    # 파일.close() : 파일닫기
except:
    print("예외가 발생했습니다.")
finally:
    file.close() # 파일.close(): 파일닫기

# 문제풀이
# 확인문제 
# 1. 구문오류(Syntax Error)와 예외(Exception)의 차이를 설명해보세요.
# 구문 오류는 문법이 잘못되어 프로그램이 실행되지 않는 오류이고, 
# 예외는 문법에는 문제가 없지만 프로그램 실행 도중 발생하는 오류이다.
# 2.
numbers = [52, 273, 32, 103, 90, 10, 275]

print("# (1) 요소 내부에 있는 값 찾기")
print("- {}는 {} 위치에 있습니다.".format(52, numbers.index(52)))
print()

print("# (2) 요소 내부에 없는 값 찾기")
number = 10000

try:
    print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))
except ValueError:
    print("- 리스트 내부에 없는 값입니다.")

print()
print("--- 정상적으로 종료되었습니다. ---")

# 3. 다음 구문에 맞는 답안을 선택하고 예외발생 시 예상 에러명 작성
output = 10 + "개"  # 1 예외 / TypeError
int("안녕하세요")    # 2 예외 / ValueError
cusor.close)        # 3 구문 오류 / SyntaxError
[1,2,3,4,5][10]     # 4 예외 / IndexError

try:
    number = int("abc")
    print("A")
except IndexError:
    print("B")
except ValueError:
    print("C")

print("D")