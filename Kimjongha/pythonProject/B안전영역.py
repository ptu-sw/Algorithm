# https://www.acmicpc.met/problem/2468
# 안전영역


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
max_height = max(map(max, area))  # 지역의 최대 높이

# 상, 하, 좌, 우 방향으로 이동하기 위한 배열
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, height):
    if x < 0 or x >= n or y < 0 or y >= n or visit[x][y] or area[x][y] <= height:
        return
    visit[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        dfs(nx, ny, height)

max_area = 0
for height in range(max_height + 1):
    visit = [[False for _ in range(n)] for _ in range(n)]
    safe_areas = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] > height and not visit[i][j]:
                dfs(i, j, height)
                safe_areas += 1
    max_area = max(max_area, safe_areas)

print(max_area)