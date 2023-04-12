# 소트인사이드
import sys
input = sys.stdin.readline

str = input().split()
str = list(map(int, str[0]))
str.sort(reverse=True)
print(*str, sep='')
