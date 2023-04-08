# 배열 합치기
import sys
input = sys.stdin.readline

ans = []  # 정답 배열
n, m = map(int, input().split())
a = list(map(int, input().split()))  # A 배열 입력
b = list(map(int, input().split()))  # B 배열 입력

ans = a + b  # a, b 합치기
ans.sort()  # 정렬
print(*ans)  # 원소 하나씩 출력
