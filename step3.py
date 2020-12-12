# coding=utf-8
# 3단계- 루빅스 큐브 구현

# CUBE 출력
def print_graph():
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
#
# def rotate_up():


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
    print_graph()
    count = 0

    # CUBE 입력 받기
    while True:
        res = input('CUBE> ')
        # 종료 조건
        if res.startswith("Q"):
            print("경과시간: ")
            print("조작갯수: "+str(count))
            print("큐브를 종료합니다...")
            break

        res = list(map(str, res.split()))
        count = len(res)



