# 요세푸스 문제
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
List = []

# 리스트에 1 ~ n 차례대로 삽입
for i in range(n):
    List.append(i + 1)

print('<', end='')
# now는 현재 인덱스
now = k - 1
for i in range(n):
    # 현재 인덱스가 List의 길이를 넘을 경우
    if now >= len(List):
        now %= len(List)

    # 마지막 수일 경우
    if len(List) == 1:
        print(List[now], end='>')
    else:
        print(List[now], end=', ')
        List.pop(now)
    # 현재 인덱스에 k만큼 더해줘야 하는데 이미 수 하나를 pop했기 때문에 k - 1
    now += k - 1

# print("<",", ".join(answer)[:],">", sep='')

# join 함수
# '구분자'.join(리스트) -> 리스트를 문자열로 만들어 주는데 문자 사이사이에 구분자를 삽입

# end & sep
# end는 출력만 마지막에 설정된 값을 출력할 때 사용
# sep는 출력문 사이사이 설정된 값을 출력할 때 사용

print('a', 'b', 'c', 'd', end='끝')  # a b c d끝
print('a', 'b', 'c', 'd', sep='*')  # a*b*c*d

# spread 연산자
ex = ['A', 'B', 'C']
print(ex, sep='-')
print(*ex, sep='-')
