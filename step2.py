# coding=utf-8
# 2단계- 평면 큐브 구현
# import sys
#
# sys.stdin = open("input2.txt", "rt")

if __name__ == "__main__":

    # 3X3 배열 만들기
    g = [[0] * 3 for _ in range(3)]
    for i in range(3):
        g[i][0], g[i][1], g[i][2] = map(str, input().split())

    # 처음 배열 출력
    for i in range(3):
        for j in range(3):
            print(g[i][j], end=' ')
        print()

    # CUBE 입력 받기
    while True:
        try:
            res = input('CUBE> ')
            if res == 'Q':
                print("Bye~")
                break
            print(res)




        except:
            break
