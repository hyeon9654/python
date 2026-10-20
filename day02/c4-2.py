# p.217 딕셔너리
# 딕셔너리란? { }중괄호 선언하고 키:값 형태로 쉼표로 연결
# { key:value , key:value , key:value }
# key 중복X / value 중복O
# JS:JSON , JAVA:MAP/DTO , DB:RECORD

# 1. 선언 , { key:value,  key:value }
dict_a = { 'name' : '어벤저스 엔드게임',
          'type': '히어로 무비'}
# 2. 값 호출, 딕셔너리명['key']
print( dict_a['name'])  # 어벤저스 엔드게임
print( dict_a['type'])  # 히어로 무비
# 3. 속성값 추가, 딕셔너리명['새로운 키'] = 새로운 값
dict_a[ 'price' ] = 5000
print( dict_a )
# 4. 속성값 수정
dict_a['type'] = '호러 무비' # 이미 존재하는 키는 수정
print( dict_a )
# 5. 속성 삭제, del 딕셔너리[ 'key' ]
del dict_a['price']
print( dict_a )
# 6. 딕셔너리내부확인 , 찾을키 in 딕셔너리명
print( 'price' in dict_a )  # False
print( 'name' in dict_a )   # True  
# 7. 속성값 호출, 방법1: 딕셔너리명['key'], 방법2: 딕셔너리명.get(key)
# 차이점 : 방법1은 존재하지 않으면 예외발생, 방법2는 존재하지 않으면 None 반환
print( dict_a.get('name'))  #어벤저스 엔드게임
print( dict_a.get('price')) # None

# 8. for 반복문과 딕셔너리 , 딕셔너리 내 key하나씩 for에서 순회
# for key반복변수 in 딕셔너리명:
#           실행코드
for key in dict_a:
            print(dict_a.get(key))  # 방법1
            print(dict_a[key])      # 방법2

numbers = [273,103,5,32,65,9,72,800,99]

for number in numbers:
        number = str(number)
        x = len(number)
        print(number,"는",x,"자릿수입니다.")

numbers = [1,2,3,4,5,6,7,8,9]
output = [ [], [], [] ]

for number in numbers:
        output[(number-1)%3].append(number)
print(output)

numbers = [ 1,2,3,4,5,6,7,8,9 ]

for i in range(0, len(numbers) // 2 ): # i는 0~3까지 나옴
        # j 가 1,3,5,7이 나오려면 어떤 식을 사용해야 하는가
        # j는 9미만 숫자 중에서 홀수만 출력한다.
        j = i * 2 + 1
        print(f"i={i},j={j}")
        numbers[j] = numbers[j] ** 2
        
print(numbers)

# i = 0 , j = 1 
# i = 1 , j = 3
# i = 2 , j = 5
# i = 3 , j = 7
[1,4,3,16,5,36,7,64,9] # numbers[j] = numbers[j]**2 여기 숫자엔 홀수값은 그대로 출력되어 해당 식에 적용되지 않는다.