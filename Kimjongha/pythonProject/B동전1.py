# https://www.acmicpc.net/problem/2293


#동전 1 2293번
#n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.


# 동적 계획법 즉 DP를 사용하는문제.




# 입력 받기
n, k = map(int, input().split())  # n과 k를 입력 받음
coins = [int(input()) for _ in range(n)]  # 각 동전의 가치를 입력 받아 리스트에 저장
# dp 테이블 초기화 (0원을 만드는 경우는 1가지로 초기화)
dp = [0] * (k + 1)
dp[0] = 1

# 각 동전에 대하여
for coin in coins:
    # coin부터 k까지 (해당 동전을 사용하여 만들 수 있는 가치)
    for value in range(coin, k + 1):
        # 현재 가치(value)를 만드는 경우의 수에,
        # 현재 동전(coin)을 제외하고 (value-coin)을 만드는 경우의 수를 더한다.
        dp[value] += dp[value - coin]

# k원을 만드는 경우의 수 출력
print(dp[k])
