# Rubik's Cube Solution

## step-1
##### 단어 밀어내기 구현하기    

<결과 화면>   
![result_step1](./result/result_step1.png)     

입력 값으로 단어(word), 정수(n), 방향(direction)을 입력받는다.    

<n 의 처리 >     
n의 값이 음수면 chk 변수에 체크를 해준다.   
n의 값이 word의 길이보다 길거나 같을 경우 처리를 해준다.   

<direction 값의 처리>        
입력으로 받은 방향의 값에 따라 각각 함수를 구현하였다.     
direction ==  L 또는 l : rotate_left()를 호출한다.   
만약 앞에서 n이 음수일 때 체크한 chk 변수가 1이면 rotate_right()을 호출한다.   
word를 왼쪽으로 밀어내는 구현은 큐(queue)를 사용하여 구현하였다.    
```
def rotate_left():
    global n, word
    q = deque(list(word))

    while n > 0:
        n -= 1
        alpha = q.popleft()
        q.append(alpha)

    q = list(q)
    res = ''

    for x in q:
        res += x
    print(res)
```

direction ==  R 또는 r : rotate_right()를 호출한다.   
만약 앞에서 n이 음수일 때 체크한 chk 변수가 1이면 rotate_left()을 호출한다.   
word를 오른쪽으로 밀어내는 구현은 stack을 사용하여 list의 가장 오른쪽에 있는 값을 pop하고 다시 list의 0번 index에 insert하는 방향으로 구현하였다.   
    
```
def rotate_right():
    global n, word
    stack = list(word)

    while n > 0:
        n -= 1
        alpha = stack.pop()
        stack.insert(0, alpha)

    res = ''

    for x in stack:
        res += x
    print(res)
```

