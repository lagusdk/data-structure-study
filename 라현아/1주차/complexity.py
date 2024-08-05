# n! 계산 알고리즘

# 1. 상수 공간 복잡도 O(1)
x = 1
n = 5
for i in range(1, n + 1):
    x = x * i

# 2. 선형 공간 복잡도 O(n)
x = 1
n = 5
a_list = []
for i in range(1, n + 1):
    a_list.append(x)
    x = x * i