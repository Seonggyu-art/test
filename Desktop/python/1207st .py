# 숫자형 : 정수(10), 실수(10.5)
# 문자열 : "Hello"

# # 정수형
# x = 10
# y = -3
# print(type(x))  # <class 'int'>
# print(x + y)    # 7

# # 실수형
# pi = 3.14159
# radius = 5
# area = pi * (radius ** 2)
# print(type(pi))  # <class 'float'>
# print(area)      # 78.53975

# 숫자형 계산
#  두 숫자의 합과 곱을 구하기
# x = 7
# y = 3
# print("덧셈 :", x + y)
# print("뺄셈 :", x - y)

# # 나머지와 몫 구하기
# print("나머지 :", x % y)
# print("몫 :", x // y)

# z = 4 + 5j
# print("실수부 :", z.real) # z_real은 그릇이고 z.real에서 .은 객체와 속성을 연결
# print("허수부 :", z.imag)

# # 문자열
# # 문자 데이터를 표현하며 '' , ""로 감싼다.
# name = "seong gyu"
# greeting = "hello"
# print(greeting, "," , name, "!")
# #문자열 반복
# print("python! " * 3)

# 리스트
# 여러 값을 저장하며, 순서를 유지하고 값 수정이 가능하다.
# fruits = ["apple", "banana", "cherry"]     # []는 리스트를 정의하는데 사용되는 기호.
# print(fruits[0])             # 리스트는 데이터를 순서대로 모아 놓는 자료형.
# print(fruits[-1])          # [] 안에 여러 값을 넣으면, 그 값이 순서대로 저장됨. 쉼표로 구분 가능.
                             
# 리스트에서 특정 값을 찾아 제거, remove
# fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana")
# print(fruits)

# 다른 예시, pop(), 은 
# pop()는 인덱스로 값을 제거하고, 그 값을 반환한다.
# 만약 인덱스를 지정하지 않으면 마지막 값이 삭제.
# fruits = ["apple", "banana", "cherry"]
# removed_item = fruits.pop(1) # 1번 인덱스 삭제
# print(fruits)                # 사과랑 체리가 나옴.
# print(removed_item)          # 바나나 나옴.

# 잠깐 설명, 인덱스란, 리스트 안의 요소(값)가 위치를 나타내는 번호
# 리스트의 첫번째 요소는 인덱스 0번부터 시작, 그다음 요소는 1,2,3 이런식으로 번호 매겨짐.
# 음수를 사용하면 뒤에서부터 접근 가능(-1이 마지막 요소)
# 인덱스를 따로 지정하지 않으면 마지막 값을 제거

# remove와 pop 비교
# pop은 인덱스로 요소를 제거.
# 특정 위치의 값을 제거하거나, 마지막 값을 제거할 때 유용.
# remove는 값으로 요소를 제거.
# 리스트에 해당 값이 여러 개 있다면, 첫 번째로 찾은 값만 제거.

# # pop() 연습문제.

# 1번 리스트에서 30제거
# li = [10, 20, 30, 40]
# li.pop(2)
# print(li)

# 2번 리스트에서 green 제거
# li = ["red", "green", "blue", "yellow"]
# li.pop(1)
# print(li)

# 3번 abcd 중 마지막 값을 제거
# li = ["a", "b", "c", "d"]
# li.pop()
# print(li)

# 리스트 값 수정
# fruits = ["apple", "banana", "cherry"]
# fruits[1] = "blueberry"
# print(fruits) # 바나나가 사라지고 블루베리가 그 자리를 차지하게 됨.

# 리스트 슬라이싱
# num = [0,1,2,3,4,5,6,7,8,9]
# print(num[2:6])  # 왼쪽은 0부터 세고 오른쪽은 1부터 세는거임.
# print(num[:5])   # 0번부터 쭉 세는거
# print(num[::-1]) # 리스트를 거꾸로 세면서 출력
# print(num[::])

# 리스트 연산
# # 1) 리스트 합치기
# li1 = [1,2,3]
# li2 = [4,5,6]
# print(li1 + li2)
# # 2) 리스트 반복
# print(li1 * 3)
# # 3) 길이 확인
# print(len(li1))  

# 잠깐 설명, len(), 리스트의 요소 개수를 반환한다. 리스트 안에 몇개고 확인할 때 사용.
# len( )함수는 리스트으 길이 뿐만 아니라 문자열, 튜플, 딕셔너리 등 다양한 자료형에서 사용.
# len()을 사용한 예제

# for 반복문이란
# 리스트나 범위 안의 모든 값을 하나씩 꺼내서 처리할 때 사용하는 반복문.
# 기본 문법
# for 변수 in 리스트:
#     실행할 코드

# for을 사용한 예시문제:
# li = [1, 2,3,4,5]
# for i in li:       
#     print(i)   # 이렇게 하면, 하나씩 하나씩 순번대로 나옴.


# range() 함수란
# 숫자의 범위를 생성하는 함수  , 시작값 : 기본 0, 간격 : 기본 1
# range(끝값, 0부터 순번)
# range(시작값, 끝값)
# range(시작값, 끝값, 간격)

# range를 이용한 예시 문제
# for i in range(5):      # 0번부터 5번째까지 차례대로 나옴.
#     print(i)

# for i in range(2,6):      # 2번부터 6번까지 차례대로 나옴.
#     print(i)

# for i in range(1,10,2):    # 1번을 시작해서 10번까징인데, 간격은 두칸씩
#     print(i)


# 헷갈리는거 range(,)와 num[:]에 차이가 있나? 다르다.
# num[]은 리스트의 특정 값(요소)에 접근하는 방법
# range()는 연속된 숫자 범위를 생성하는 함수. 하나씩 값이 생성되는 객체

# range() 간격을 음수로 지정
# for i in range(10, 0, -2):   # 10부터 0까지 숫자가 감소하는 범위를 생성
#     print(i)

# range()를 리스트로 변환하기
# range()는 숫자를 생성하지만, 리스트처럼 보이지 않는다.
# list()를 사용해 숫자들을 리스트로 변환할 수 있다.
# 예시 :
# r = range(5)
# print(r)
# print(list(r))


# 헷갈리는거 range(5) 그동안 출력될 때 0부터 4까지 출력인데, 바로 위는 다르다.
# range()와 리스트의 차이
# 1. range()는 숫자를 생성하는 설계도 같은것
# range()는 숫자의 나열을 필요할 때 생성하는 객체.
# 하지만 실제로 숫자들을 저장하지 않기 때문에, 리스트처럼 바로 보이지 않는다.
# r = range(5)
# print(r)  # 출력: range(0, 5)
# range(0, 5)는 0부터 5 직전까지 숫자를 생성할 준비가 된 상태를 의미.
# 2. 리스트는 숫자를 저장하고 바로 보여줌.
# 리스트는 모든 값을 즉시 메모리에 저장하고, 바로 출력할 수 있다.
# numbers = [0,1,2,3,4]
# print(numbers)
# 3. 왜 range()와 리스트는 다르게 보이는가
#  - range()는 숫자 범위를 만들 준비는 했지만, 실제 값을 저장하지는 않음.
#  - 리스트는 숫자들을 이미 저장하고 있음.
# range()를 리스트처럼 보고 싶다면, 리스트 함수를 이용해서 range()를 리스트로 변환해야 함.
# r = range(5)
# print(list(r))
# range()는 숫자를 필요할 때만 생성하기 때문에 메모리를 효율적으로 사용.

# 리스트에 값 추가
# append() 메서드
# 값을 리스트 맨 끝에 추가.
# 사용법 : 리스트.append(값)

# 예시 :
# fruits = ["aplle", "banana"]
# fruits.append("cherry")
# print(fruits)

# insert() 매서드
# 리스트의 특정 위치에 값을 삽입한다.
# 사용법 : 리스트.insert(인덱스, 값)

# 예시 :
# fruits = ["apple", "cherry"]
# fruits.insert(1, "banana")    # 1번 인덱스에 삽입한다.
# print(fruits)
# num = [1,2,3,4,5]
# for i in range

# 리스트에서 값 삭제, del 키워드
# 리스트의 특정 위치 값을 삭제
# 사용법 : del 리스트[인덱스]

# 예시 :
# numbers = [1,2,3,4]
# del numbers[2]  # 2번 인덱스 값 삭제
# print(numbers)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 조건문이란
# 특정 조건에 따라 실행할 코드를 결정하는 방법
# 만약에 조건이 참이면 이코드를 실행해.라는 기능

