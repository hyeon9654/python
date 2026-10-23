# 예외객체란? 발생한 예외 정보 갖는 객체
# 예외클래스 : Exception(예외 최상위클래스)
# except 예외클래스명 as 변수명 :
# raise : 강제로 예외발생 , 주로 CRUD 실패 500의미
# p.383
list_number=[ 52, 273, 32, 72, 100 ]
try:
    number_input = int(input('정수입력:'))  # 타입 예외
    print( list_number[ number_input ] )   # 인덱스 예외
    raise NotImplementedError
    # java: throws new 예외클래스()
except ValueError as e:     # 타입변환 예외
    print(e)
except IndexError as e:     # 인덱스 예외 
    print(e)
except Exception as e:      # 그외 (최상위) 예외 항상 마지막
    print(e) 


# 연습문제 
numbers = [ 52,273,32,103,90,10,275 ]

print("#(1) 요소 내부에 있는 값 찾기")
print("-{}는 {} 위치에 있습니다.".format(52,numbers.index(52)))
print()

print("#(2) 요소 내부에 없는 값 찾기")
number = 10000
try:
    print("- {}는 {} 위치에 있습니다.".format(number, numbers.index(number)))

except ValueError:
    print("-리스트 내부에 없는 값입니다.")


# 연습문제
output = 10 + "개"  # 타입에러
int("안녕하세요")    # 타입에러 
cusur.close)        # 밸류에러
[1,2,3,4,5][10]     # 구문오류