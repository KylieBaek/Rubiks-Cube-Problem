# coding=utf-8
# 2단계- 루빅스 큐브 구현


if __name__ == "__main__":
    # 큐브 초기 상태
    g = [[0] * 3 for _ in range(6)]
    # Front
    g[0] = [['O', 'O', 'O'] for _ in range(3)]
    # Back
    g[1] = [['Y', 'Y', 'Y'] for _ in range(3)]
    # Left
    g[2] = [['W', 'W', 'W'] for _ in range(3)]
    # Right
    g[3] = [['G', 'G', 'G'] for _ in range(3)]
    # Up
    g[4] = [['B', 'B', 'B'] for _ in range(3)]
    # Down
    g[5] = [['R', 'R', 'R'] for _ in range(3)]
