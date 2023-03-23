# <> 내부 문자열은 정상 출력
# <> 외부 문자열은 거꾸로 출력 => str[::-1]
# 문자를 하나하나 입력하고 > 를 만나면 정상 출력
# 태그 안 일 때와 태그 밖일 때를 구분
import sys
input = sys.stdin.readline

str = input()
substr = ''  # 부분 문자열
now = ''  # 현재 태그 안인지 밖인지를 나타내는 문자열
ans = ''  # 정답 문자열

for ch in str:
    if ch == '<':
        ans += substr[::-1]
        ans += '<'
        substr = ''
        now = '<'

    # 태그 안 공백이라면
    elif ch == ' ' and now == '<':
        ans += substr
        ans += ' '
        substr = ''

    # 태그 밖 공백
    elif ch == ' ' and (now == '>' or now == ''):
        ans += substr[::-1]
        ans += ' '
        substr = ''

    elif ch == '>':
        now = '>'
        ans += '>'

    # 태그 안 문자
    elif now == '<':
        ans += ch

    # 태그 밖 문자
    elif now == '>' or now == '':
        substr += ch

print(ans + substr.replace("\n", "")[::-1])
