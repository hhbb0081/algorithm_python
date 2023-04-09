# 단어 공부
import sys
input = sys.stdin.readline

cnt = [0] * 26
str = input().split()  # 배열에 담김
for ch in str[0]:
    if (ord(ch) >= 65 and ord(ch) <= 90):
        print(ord(ch) + 32, end=' ')  # 대문자를 소문자로 변환
        cnt[ord(ch) - 65] += 1
    else:
        print(ord(ch), end=' ')
        cnt[ord(ch) - 97] += 1

Max = 0
ans = 0
for i in range(len(cnt)):
    if cnt[i] == 0:
        continue
    elif cnt[i] > Max:
        Max = cnt[i]
        ans = i
print(chr(ans + 65))
