# coding=utf-8
# 2단계- 평면 큐브 구현
from collections import deque
import copy


def rotate_left(arr, n):
    arr = copy.deepcopy(arr)
    q = deque(arr)
    # 왼쪽으로 밀기
    while n > 0:
        n -= 1
        alpha = q.popleft()
        q.append(alpha)

    q = list(q)
    return q


def rotate_right(arr, n):
    stack = copy.deepcopy(arr)
    # 오른쪽으로 밀기
    while n > 0:
        n -= 1
        alpha = stack.pop()
        stack.insert(0, alpha)

    return stack


def print_graph(inp):
    print(inp)
    for k in range(3):
        for m in range(3):
            print(g[k][m], end=' ')
        print()
    print()


if __name__ == "__main__":

    # 3X3 배열 만들기
    g = [[0] * 3 for _ in range(3)]
    for i in range(3):
        g[i][0], g[i][1], g[i][2] = map(str, input().split())

    # 처음 배열 출력
    print_graph("")

    # CUBE 입력 받기
    while True:
        res = input('CUBE> ')
        # 종료 조건
        if res.startswith("Q"):
            print("Bye~")
            break

        # 회전할 리스트 받기
        res = list(map(str, res.split()))
        input_arr = []
        output_arr = []

        for x in res:
            # 가장 윗줄 회전
            if x == "U" or x == "U'":
                input_arr = g[0]
                if x.endswith("'"):
                    output_arr = rotate_right(input_arr, 1)
                else:
                    output_arr = rotate_left(input_arr, 1)
                g[0] = output_arr

            # 가장 아랫줄 회전
            elif x == "B" or x == "B'":
                input_arr = g[2]
                if x.endswith("'"):
                    output_arr = rotate_left(input_arr, 1)
                else:
                    output_arr = rotate_right(input_arr, 1)
                g[2] = output_arr

            # 가장 오른쪽 줄 회전
            elif x == "R" or x == "R'":
                input_arr = [g[0][2], g[1][2], g[2][2]]
                if x.endswith("'"):
                    output_arr = rotate_right(input_arr, 1)
                else:
                    output_arr = rotate_left(input_arr, 1)
                for j in range(3):
                    g[j][2] = output_arr[j]

            # 가장 왼쪽 줄 회전
            elif x == "L" or x == "L'":
                input_arr = [g[0][0], g[1][0], g[2][0]]
                if x.endswith("'"):
                    output_arr = rotate_left(input_arr, 1)
                else:
                    output_arr = rotate_right(input_arr, 1)
                for j in range(3):
                    g[j][0] = output_arr[j]

            # 큐브 출력
            print_graph(x)
