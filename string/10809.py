# 알파벳 찾기
import sys
input = sys.stdin.readline

str = input().split()
ans = [-1] * 26

for i in range(len(str[0])):
    if ans[ord(str[0][i]) - 97] != -1:
        continue
    else:
        ans[ord(str[0][i]) - 97] = i
for num in ans:
    print(num, end=' ')

# find 메소드를 이용해서 해당 문자가 문자열에 존재하는지 확인
