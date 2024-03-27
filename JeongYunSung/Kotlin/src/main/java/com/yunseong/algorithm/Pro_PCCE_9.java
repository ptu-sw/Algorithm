package com.yunseong.algorithm;

public class Pro_PCCE_9 {

    public int solution(String[][] board, int h, int w) {
        int answer = 0;

        int[] dx = new int[] {0, 1, 0, -1};
        int[] dy = new int[] {-1, 0, 1, 0};

        for (int i = 0; i < 4; i++) {
            int nx = w + dx[i];
            int ny = h + dy[i];

            if (board.length <= ny || ny < 0 || board[0].length <= nx || nx < 0) {
                continue;
            }

            if (board[ny][nx].equals(board[h][w])) {
                answer++;
            }
        }

        return answer;
    }
}
