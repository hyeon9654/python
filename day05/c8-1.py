# 절차지향 프로그래밍 : 데이터를 순서대로 처리하고 하향식 순차 실행 흐름, C
# 객체지향 프로그래밍 : 객체 우선으로 생각해서 프로그래밍, JAVA/PYTHON/JS
# 관점지향 프로그래밍 : 공통되는 기능(로그/검증/보안 등)들을 분리하여 프로그래밍 설계, SPRING
# 추상화 : 핵심적인 개념 또는 기능 간추려 내는 것
# 객체 :속성명과 속성값으로 표현
# [0 리스트 ], { 딕셔너리 } 객체이다.
# 클래스: 추상화한 데이터들을 구조화 한 것( 설계도 )
# 객체: 세상에 존재하는 모든 데이터들을 추상화( 실체X )      -> 개념적 객체
# 인스턴스: 추상화한 것을 객체로 만든것( 실체O )            -> 물리적 객체
# 인스턴스화: 컴퓨터내 객체 정보 저장, JAVA: new 생성자(),  PY: 생성자()
# 생성자: 클래스 기반으로 인스턴스 만드는 함수              -> 인스턴스 초기화함수

# 1. 클래스 만들기
# 클래스를 선언합니다.
class Student:
    pass

# 학생을 선언합니다.
student = Student()     # JAVA: new Student(), PY: Student()

# 학생 리스트를 선언합니다.
student = [
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
    Student()
]

# 2. 생성자
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
# 생성자 이용한 인스턴스 생성
# JAVA : Student2 s = new Student( "유재석", 10, 20, 30, 40 )
# 학생 리스트를 선언합니다.
student = [
    Student("윤인성",87,98,88,95),
    Student("연하진",92,98,96,98),
    Student("구지연",76,96,94,90),
    Student("나선주",98,92,96,92), 
    Student("윤아린",95,98,98,98),
    Student("윤명월",64,88,92,92)
]
# Student 인스턴스의 속성에 접근하는 방법
student[0].name
student[0].korean
student[0].math
student[0].english
student[0].science

# 가비지 컬렉터★