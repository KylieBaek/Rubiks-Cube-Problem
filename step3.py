# coding=utf-8
# 3단계- 루빅스 큐브 구현


# CUBE 출력
def print_graph(m):
    print(m)
    # up 출력
    for i in range(3):
        print('      ', end='')
        for j in range(3):
            print(g[4][i][j], end='')
        print()
    print()

    # left, front, right , back 출력
    for i in range(3):
        for k in (2, 0, 3, 1):
            for j in range(3):
                print(g[k][i][j], end='')
            print('   ', end='')
        print()

    # down 출력
    print()
    for i in range(3):
        print('      ', end='')
        for j in range(3):
            print(g[5][i][j], end='')
        print()
    print()


# cube 앞면 회전
def rotate_front(direct, count):
    #  반시계 방향 회전일 때
    if direct == -1:
        count = count * 3

    count = count % 4
    if count == 0:
        return
    while count > 0:
        count -= 1
        tmp_u = [g[4][2][0], g[4][2][1], g[4][2][2]]
        tmp_r = [g[3][0][0], g[3][1][0], g[3][2][0]]
        tmp_d = [g[5][0][0], g[5][0][1], g[5][0][2]]
        tmp_l = [g[2][0][2], g[2][1][2], g[2][2][2]]

        g[4][2][0], g[4][2][1], g[4][2][2] = tmp_l
        g[3][0][0], g[3][1][0], g[3][2][0] = tmp_u
        g[5][0][0], g[5][0][1], g[5][0][2] = tmp_r
        g[2][0][2], g[2][1][2], g[2][2][2] = tmp_d


def rotate_back(direct, count):
    if direct == -1:
        count = count * 3

    count = count % 4
    if count == 0:
        return
    while count > 0:
        count -= 1
        tmp_u = [g[4][0][0], g[4][0][1], g[4][0][2]]
        tmp_r = [g[3][0][2], g[3][1][2], g[3][2][2]]
        tmp_d = [g[5][2][0], g[5][2][1], g[5][2][2]]
        tmp_l = [g[2][0][0], g[2][1][0], g[2][2][0]]

        g[4][0][0], g[4][0][1], g[4][0][2] = tmp_r
        g[3][0][2], g[3][1][2], g[3][2][2] = tmp_d
        g[5][2][0], g[5][2][1], g[5][2][2] = tmp_l
        g[2][0][0], g[2][1][0], g[2][2][0] = tmp_u


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

    # 초기 상태 큐브 출력
    print_graph("")
    operation = 0

    # CUBE 입력 받기
    while True:
        res = input('CUBE> ')
        # 종료 조건
        if res.startswith("Q"):
            print("경과시간: ")
            print("조작갯수: " + str(operation))
            print("큐브를 종료합니다...")
            break

        res = list(map(str, res.split()))
        operation = len(res)

        for x in res:
            if x.startswith("F"):
                method = x
                direction = 1
                cnt = 1

                # 회전 조건 4가지: F or F' or F'2 or F2
                if len(x) > 1:
                    x = x.split("F")[1]
                    if x.startswith("'"):
                        direction = -1
                        if len(x) > 1:
                            cnt = int(x.split("'")[1])
                    else:
                        cnt = int(x)

                rotate_front(direction, cnt)
                print_graph(method)

            elif x.startswith("B"):
                method = x
                direction = 1
                cnt = 1

                if len(x) > 1:
                    x = x.split("B")[1]
                    if x.startswith("'"):
                        direction = -1
                        if len(x) > 1:
                            cnt = int(x.split("'")[1])
                    else:
                        cnt = int(x)

                rotate_back(direction, cnt)
                print_graph(method)
