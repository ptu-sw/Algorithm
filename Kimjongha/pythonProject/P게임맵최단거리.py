#https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque


#게임 맵 최단거리


def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [0, 0, -1, 1]  # 동, 서, 남, 북 방향의 x축 이동
    dy = [1, -1, 0, 0]  # 동, 서, 남, 북 방향의 y축 이동

    def bfs():
        queue = deque([(0, 0, 1)])  # 시작점과 시작점에서의 거리
        visited = set([(0, 0)])
        while queue:
            x, y, dist = queue.popleft()
            if x == n - 1 and y == m - 1:  # 도착점에 도달했다면
                return dist
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
        return -1  # 도착점에 도달할 수 없는 경우
    return bfs()


maps1 = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1]
]

maps2 = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1]
]
print(solution(maps1))  # 11
