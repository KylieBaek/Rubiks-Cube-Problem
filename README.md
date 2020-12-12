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


## step-2
##### 평면 큐브 구현하기    

<결과 화면>   
![result_step2_1](./result/result_step2_1.png)  
![result_step2_2](./result/result_step2_2.png)    

3X3의 2차원 배열 값을 입력받고 입력받은 초기 평면 큐브를 print_graph() 함수를 통해 출력해주었다.      
```
def print_graph(inp):
    print(inp)
    for k in range(3):
        for m in range(3):
            print(g[k][m], end=' ')
        print()
    print()
```

step-1과 마찬가지로 해당 리스트를 왼쪽으로 밀 때는 rotate_left(리스트, 횟수), 오른쪽으로 밀 때는 rotate_right(리스트, 함수)를 호출하였다.   
전역 변수의 사용을 최소화하기 위해 copy 모듈의 deepcopy()를 사용하여 매개변수로 받은 리스트를 새로운 리스트를 복사해주었다.     
```
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
```
 
input() 함수를 사용하여 입력받을 때 'CUBE> '를 표시해주었다.   
while문은 "Q"가 입력될 때 종료된다.   
 ```
 while True:
        res = input('CUBE> ')
        # 종료 조건
        if res.startswith("Q"):
            print("Bye~")
            break
```

while 문에서 res의 값이 "Q"가 아닐 때는 res를 list 형으로 바꿔준다.     
해당 조건 (U, B, R, L)에 따라서 회전할 list를 input_arr에 담아서 rotate 함수를 호출한다.       
rotate 함수는 회전된 list를 리턴한다.      
리턴된 output_arr을 평면 큐브 g에 변경해준다.   
 ```
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

```
