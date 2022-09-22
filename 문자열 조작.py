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
s = "A men, a plan, a canal : Panama"
"race a car"

# 리스트로 변환
strs = []
for char in s:
    if char.isalnum(): # isalnum() : 영문자, 숫자 여부를 판별하는 함수
        strs.append(char.lower())

strs # 리스트에 담긴다. 한 글자씩

while len(strs) > 1:
    if strs.pop(0) != strs.pop():
        return False
# 이렇게 하면 syntaxError가 뜨는데 while문이 함수에 포함되어 있지 않아서 그렇다고 한다.

def isPalindrome(self, s: str) -> bool :
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

isPalindrome()