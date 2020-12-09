# coding=utf-8
# 1단계- 단어 밀어내기 구현


if __name__ == "__main__":
    word, n, direction = map(str, input().split())

    # 음수 확인
    chk = 0
    if n.startswith('-'):
        chk = 1
        n = int(n.split('-')[1])
    else:
        n = int(n)
