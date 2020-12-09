# coding=utf-8
# 1단계- 단어 밀어내기 구현
from collections import deque


# 방향에 따라서 함수 구현
def rotate_left():
    global n, word
    q = deque(list(word))

    if n == len(word):
        print(word)
        return
    elif n > len(word):
        n = n % len(word)

    while n > 0:
        n -= 1
        alpha = q.popleft()
        q.append(alpha)

    q = list(q)
    res = ''

    for x in q:
        res += x
    print(res)


if __name__ == "__main__":
    word, n, direction = map(str, input().split())

    # 음수 확인
    chk = 0
    if n.startswith('-'):
        chk = 1
        n = int(n.split('-')[1])
    else:
        n = int(n)

    rotate_left()
