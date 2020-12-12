# coding=utf-8
# 3단계- 루빅스 큐브 구현
import time
import copy
import random


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


# CUBE 회전 조건 반환 함수
def get_condition(m):
    direct = 1
    count = 1

    # 회전 조건 4가지 예: F or F' or F'2 or F2
    if len(m) > 1:
        m = m.split(m[0])[1]
        if m.startswith("'"):
            direct = -1
            if len(m) > 1:
                count = int(m.split("'")[1])
        else:
            count = int(m)
    return direct, count


# CUBE 한 면 회전
def rotate_full(i):
    # 모서리 회전
    tmp = g[i][0][0]
    g[i][0][0] = g[i][2][0]
    g[i][2][0] = g[i][2][2]
    g[i][2][2] = g[i][0][2]
    g[i][0][2] = tmp

    # 엣지 회전
    tmp = g[i][0][1]
    g[i][0][1] = g[i][1][0]
    g[i][1][0] = g[i][2][1]
    g[i][2][1] = g[i][1][2]
    g[i][1][2] = tmp


# CUBE 앞면 회전
def rotate_front(count):
    while count > 0:
        count -= 1
        tmp_u = [g[4][2][0], g[4][2][1], g[4][2][2]]
        tmp_r = [g[3][2][0], g[3][1][0], g[3][0][0]]
        tmp_d = [g[5][0][0], g[5][0][1], g[5][0][2]]
        tmp_l = [g[2][2][2], g[2][1][2], g[2][0][2]]

        g[4][2][0], g[4][2][1], g[4][2][2] = tmp_l
        g[3][0][0], g[3][1][0], g[3][2][0] = tmp_u
        g[5][0][0], g[5][0][1], g[5][0][2] = tmp_r
        g[2][0][2], g[2][1][2], g[2][2][2] = tmp_d
        rotate_full(0)


# CUBE 뒷면 회전
def rotate_back(count):
    while count > 0:
        count -= 1
        tmp_u = [g[4][0][0], g[4][0][1], g[4][0][2]]
        tmp_r = [g[3][0][2], g[3][1][2], g[3][2][2]]
        tmp_d = [g[5][2][0], g[5][2][1], g[5][2][2]]
        tmp_l = [g[2][0][0], g[2][1][0], g[2][2][0]]

        g[4][0][0], g[4][0][1], g[4][0][2] = tmp_r
        g[3][2][2], g[3][1][2], g[3][0][2] = tmp_d
        g[5][2][0], g[5][2][1], g[5][2][2] = tmp_l
        g[2][2][0], g[2][1][0], g[2][0][0] = tmp_u
        rotate_full(1)


# CUBE 윗면 회전
def rotate_up(count):
    while count > 0:
        count -= 1
        tmp_l = g[2][0]
        tmp_f = g[0][0]
        tmp_r = g[3][0]
        tmp_b = g[1][0]

        g[2][0] = tmp_f
        g[0][0] = tmp_r
        g[3][0] = tmp_b
        g[1][0] = tmp_l
        rotate_full(4)


# CUBE 아랫면 회전
def rotate_down(count):
    while count > 0:
        count -= 1
        tmp_l = g[2][2]
        tmp_f = g[0][2]
        tmp_r = g[3][2]
        tmp_b = g[1][2]

        g[2][2] = tmp_b
        g[0][2] = tmp_l
        g[3][2] = tmp_f
        g[1][2] = tmp_r
        rotate_full(5)


# CUBE 왼쪽면 회전
def rotate_left(count):
    while count > 0:
        count -= 1
        tmp_u = [g[4][0][0], g[4][1][0], g[4][2][0]]
        tmp_f = [g[0][0][0], g[0][1][0], g[0][2][0]]
        tmp_d = [g[5][2][0], g[5][1][0], g[5][0][0]]
        tmp_b = [g[1][2][2], g[1][1][2], g[1][0][2]]

        g[4][0][0], g[4][1][0], g[4][2][0] = tmp_b
        g[0][0][0], g[0][1][0], g[0][2][0] = tmp_u
        g[5][0][0], g[5][1][0], g[5][2][0] = tmp_f
        g[1][0][2], g[1][1][2], g[1][2][2] = tmp_d
        rotate_full(2)


# CUBE 오른쪽면 회전
def rotate_right(count):
    while count > 0:
        count -= 1
        tmp_u = [g[4][2][2], g[4][1][2], g[4][0][2]]
        tmp_f = [g[0][0][2], g[0][1][2], g[0][2][2]]
        tmp_d = [g[5][0][2], g[5][1][2], g[5][2][2]]
        tmp_b = [g[1][2][0], g[1][1][0], g[1][0][0]]

        g[4][0][2], g[4][1][2], g[4][2][2] = tmp_f
        g[0][0][2], g[0][1][2], g[0][2][2] = tmp_d
        g[5][0][2], g[5][1][2], g[5][2][2] = tmp_b
        g[1][0][0], g[1][1][0], g[1][2][0] = tmp_u
        rotate_full(3)


# CUBE 무작위 섞기
def rotate_random():
    rotate_right(random.randrange(1, 4))
    rotate_left(random.randrange(1, 4))
    rotate_up(random.randrange(1, 4))
    rotate_down(random.randrange(1, 4))
    rotate_front(random.randrange(1, 4))
    rotate_back(random.randrange(1, 4))


if __name__ == "__main__":
    # 프로그램 시작 시간
    start_time = time.time()
    # 초기 상태 큐브
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
    init_g = copy.deepcopy(g)
    init_chk = 0

    # CUBE 입력 받기
    while True:
        if init_chk == 1:
            break
        res = input('CUBE> ')
        # 종료 조건
        if res.startswith("Q"):
            duration = round(time.time() - start_time, 2)
            print("경과시간: " + str(duration) + "s")
            print("조작갯수: " + str(operation))
            print("큐브를 종료합니다...")
            break

        if res == "mix":
            rotate_random()
            print_graph("무작위로 큐브 섞기!!")
            continue

        res = list(map(str, res.split()))

        for x in res:
            # 조작 갯수 카운트
            operation += 1
            # 회전 방향, 회전 횟수 조건 설정
            direction, cnt = get_condition(x)
            # 반시계 방향일 경우
            if direction == -1:
                cnt = cnt * 3

            cnt = cnt % 4
            if cnt == 0:
                print_graph(x)
                continue

            if x.startswith("F"):
                rotate_front(cnt)
            elif x.startswith("B"):
                rotate_back(cnt)
            elif x.startswith("U"):
                rotate_up(cnt)
            elif x.startswith("D"):
                rotate_down(cnt)
            elif x.startswith("L"):
                rotate_left(cnt)
            elif x.startswith("R"):
                rotate_right(cnt)

            # 회전된 CUBE 출력
            print_graph(x)

            # 모든 면을 맞추면 종료
            if init_g == g:
                print("축하합니다! 모든 면을 맞추셨어요. 큐브를 종료합니다...")
                init_chk = 1
                break
