# 문자열 조작
'''
1. 정보 처리 분야
    어떤 키워드로 웹 페이지를 탐색할 때 문자열 처리 애플리케이션을 이용하게 된다.
    특히 현대의 거의 모든 정보는 문자열로 구성되어 있으며 문자열 처리는 정보 처리에
    핵심적인 역할을 한다.
2. 통신 시스템 분야
    문자 메시지나 이메일을 보낼 때 기본적으로 문자열을 어느 한 곳에서 다른 곳으로 보내게 된다.
    이처럼 데이터 전송은 문자열 처리 알고리즘이 탄생한 기원이기도 하며, 데이터 전송에서
    문자열 처리는 매우 중요한 역할을 한다.
3. 프로그래밍 시스템 분야
    프로그램은 그 자체가 문자열로 구성되어 있다. 컴파일러나 인터프리터 등은
    문자열을 해석하고 처리하여 기계어로 변환하는 역할을 하며, 여기에는
    매우 정교한 문자열 처리 알고리즘 등이 쓰인다.
'''

# 유효한 팰린드롬
# 팰린드롬 - 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장을 말한다.
# 대소문자를 구분하지 않으며, 영문자와 숫자 만을 대상으로 한다.

# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
import re

s = "A man, a plan, a canal : Panama"
"race a car"

# 리스트로 변환
strs = []
for char in s:
    if char.isalnum(): # isalnum() : 영문자, 숫자 여부를 판별하는 함수
        strs.append(char.lower())  # lower() : 소문자로 만들어주기

strs # 리스트에 담긴다. 한 글자씩

while len(strs) > 1:
    if strs.pop(0) != strs.pop():
        return False
# 이렇게 하면 syntaxError가 뜨는데 while문이 함수에 포함되어 있지 않아서 그렇다고 한다.

def isPalindrome(self):
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:                   # strs의 글자 길이가 1보다 클때
        if strs.pop(0) != strs.pop():      # strs의 첫번째 글자(꺼내 삭제)가 strs의 마지막 글자(꺼내 삭제)와 같지 않으면
            return False                   # false를 출력해라

    return True                            # 그렇지 않으면 true를 출력해라 (즉 같으면 true 출력)

isPalindrome(s)

# 데크 자료형을 이용한 최적화
# 데크 - 리스트와 같이 요소들을 한 곳에 담아두는 배열이다.
# 데크를 이용하면 더 빨라진다 라고만 알고있자
from collections import deque  # 왜 안될까...

def isPalindrome(self):
    # 자료형 데크로 선언
    strs : Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

# 슬라이싱을 사용한 문제 풀이

s = "A man, a plan, a canal : Panama"

import re

def ispalindrome(self):
    s = s.lower()  # 이 s는 왜 인식이 안되는걸까
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]','',s)
    return s == s[::-1] # 슬라이싱 / [::-1] 뒤집기

ispalindrome(s)

a = "안녕하세요"
a[1:4] # 인덱스 1에서 4이전까지
a[1:-2] # 인덱스 1에서 -2 이전까지 (-2는 포함x)
a[1:100] # 인덱스가 크면 최대길이만큼만 표현
a[-1] # 마지막 문자(뒤에서 첫번째)
a[:-3] # 뒤에서 3개 글짜 앞까지
a[-3:] # 뒤에서 3번째 문자에서 마지막까지
a[::1] # 1은 기본값으로 동일하다.
a[::-1] # 뒤집는다.
a[::2] # 2칸씩 앞으로 이동한다.

# 문자열 뒤집기
# 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 라스트 내부를 직접 조작하라.
