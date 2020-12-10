# coding=utf-8
# 2단계- 평면 큐브 구현
from collections import deque
import copy


def rotate_left(arr):
    arr = copy.deepcopy(arr)
    q = deque(arr)
    # 왼쪽으로 한 칸 밀기
    alpha = q.popleft()
    q.append(alpha)

    q = list(q)
    return q


def rotate_right(arr):
    stack = copy.deepcopy(arr)
    # 오른쪽으로 한 칸 밀기
    alpha = stack.pop()
    stack.insert(0, alpha)

    return stack


# def rotate_list(arr, direction):
#     if direction == 'l':
#         result = rotate_left(arr)
#     elif direction == 'r':
#         result = rotate_right(arr)
#     return result

def print_graph():
    global g
    for k in range(3):
        for m in range(3):
            print(g[k][m], end=' ')
        print()


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

        res = input('CUBE> ')
        if res == "Q":
            print("Bye~")
            break

        # 회전할 리스트 받기
        # '이 문자에 따라 chk 변수 만들어야함
        for x in res:
            input_arr = []
            output_arr = []

            # 가장 윗줄 회전
            if x == "U" or x == "U'":
                input_arr = g[0]
                print(input_arr)
                if x.endswith("'"):
                    output_arr = rotate_right(input_arr)
                else:
                    output_arr = rotate_left(input_arr)
                print(output_arr)
                g[0] = output_arr
                print_graph()
