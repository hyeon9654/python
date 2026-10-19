# 85p. 타입 확인하기, type( 자료 )
print(type("안녕하세요")) # <class 'str'>
print(type(123)) # <class 'int'>
print(type(1.23)) # <class 'float'>
print(type(True)) # <class 'bool'>
print(type(None)) # <class 'NoneType'>
print(type( [] )) # <class 'List'>
print(type( {} )) # <class 'dict'>
print(type( () )) # <class 'tuple'>

# 86. 문자열만들기
print("ABC")    # 큰따옴표 감싼
print('ABC')    # 작은따옴표 감싼
print("""A
B
C""")           # """ 여러줄 """ 감싼
print("A'B'C")  # 작은따옴표 출력
print('A"B"C')  # 큰따옴표 출력
print("\"A\"B\nC\tD\\E")    # 제어문자

# 93p. 문자열 연산
# 1. + 연결연산자
print("안녕"+"하세요")
# print("안녕" + 1 ) # 주의할점 : 문자열과 숫자 연결 불가능
# 2. * 반복연산자

