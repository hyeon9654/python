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
