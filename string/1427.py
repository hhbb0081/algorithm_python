# 소트인사이드
str = list(map(int, input()))
str.sort(reverse=True)
print(*str, sep='')

# input = sys.stdin.readline 사용할 경우 개행문자까지 입력됨
