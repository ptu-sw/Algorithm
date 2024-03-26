# https://www.acmicpc.net/problem/1946


#신입 사원 1946

#이문제는 서류와 면접 성적중 다른사람보다 하나라도 떨어지지않는 사람을 선발하는문제임..

# 1. 한쪽을 기준으로 먼저 정렬을 먼저하면 나머지는 찾기 쉬워지니 정렬을 먼저 해보자.
# 2  sort를 적용하므로, 처리시간이 굉장히 오래걸리는 단점이 있지만, 이렇게 그리디 알고리즘으로 해결


def max_selected_candidates(test_cases):
    results = []  # 결과를 저장할 리스트

    for _ in range(test_cases):
        n = int(input())  # 지원자 수 입력 받기
        candidates = []  # 지원자 정보를 저장할 리스트

        for _ in range(n):
            paper, interview = map(int, input().split())
            candidates.append((paper, interview))

        # 2. 지원자 정렬 (예: 서류심사 성적 기준으로 오름차순 정렬)
        candidates.sort(key=lambda x: x[0])

        # 3. 최대 인원 수 계산
        max_interview_rank = float('inf')  # 면접시험 성적의 최고 순위 (초기값: 무한대)
        selected_count = 0  # 선발된 지원자 수

        for _, interview in candidates:
            # 현재 지원자의 면접 성적이 이전 지원자들의 면접 성적 중 최고 순위보다 높은 경우
            if interview < max_interview_rank:
                selected_count += 1  # 선발 인원 수 증가
                max_interview_rank = interview  # 최고 면접 성적 순위 갱신

        results.append(selected_count)  # 이 테스트 케이스의 결과 저장

    # 4. 결과 출력
    for result in results:
        print(result)

# 입력 예제
T = int(input())  # 테스트 케이스 수 입력 받기
max_selected_candidates(T)


