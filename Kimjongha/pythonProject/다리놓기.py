#https://www.acmicpc.net/problem/1010
# 실버5


# 조합 문제 예시를 보면 왼편에 4개  오른편에 7개가 있는데
# 여기서 왼쪽이든 오른쪽이든 4개만 연결되면 되기때문데
# 조합으로 풀수있다 즉 7C4

def fac(n):    # 팩토라얼 수행
    if n ==0 or n ==1:
        return 1
    else:
        return n*fac(n-1)

def comb(a,b):
    return  int(fac(b) / (fac(a)*fac(b-a)))  #조합의 공식을 적어주고 int형으로 형변환한다.

def solve():
    a, b = [int(x) for x in input().split()] #1. 입력 받고

    print(comb(a,b))  #2. 조합 함수 생성



t = int(input())

for _ in range(t):
    solve()
