# 괄호
n = int(input())
str = [input() for _ in range(n)]

for substr in str:
    # 괄호 넣을 리스트
    bracket = []
    # 반복문 종료 여부
    end = False
    for ch in substr:
        if ch == '(':
            bracket.append('(')
        else:
            if len(bracket) > 0:
                bracket.pop(-1)
            else:
                print('NO')
                end = True
                break
    if len(bracket) == 0 and end == False:
        print('YES')
        bracket.clear()
    elif len(bracket) > 0:
        print('NO')
        bracket.clear()
