# -*- coding: utf-8 -*-

N, K = input().split()
K = int(K); N = int(N)

c = 0; a = 0; returnflag = False  # c = 카운트, a = 리스트 커서, returnflag = 커서가 첫번째로 되돌아올 시 플래그

# user_input = input().split()  # 다중입력
# user_input = ["7", "3", "1", "8", "4", "6", "2", "5"]  # 첫번째 데이터, 첫 입력은 4 3
user_input = [31, 36, 20, 30, 1, 9, 6, 13, 3, 29, 11, 25, 7, 8, 2, 24, 34, 18, 26, 15, 23, 28, 37, 19, 21, 4, 32, 14, 16, 10, 12, 27, 22, 35, 5, 17, 33]  # 번째 데이터, 첫 입력은37 4

for i in range(0, N):  # int 형으로 바꿔주기
    user_input[i] = int(user_input[i])

while N != user_input.count(min(user_input)):  # 모두 최소 수가 될때까지로
    for j in range(a, a+K):  # a부터 a+K까지 j라는 변수
        if j == N:  # 한바퀴 돌고 나서 커서 초기화
            a = 0; j = 0; returnflag = True
        else:
            user_input[j] = min(user_input[a:a+K]) if returnflag == False else min(user_input)
    a += K-1; c += 1
    # for z in range(0, K):
    #     user_input[z] = min(user_input)

print(c)