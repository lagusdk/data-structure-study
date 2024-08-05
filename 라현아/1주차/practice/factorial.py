# 1. 숫자 n의 팩토리얼을 계산하는 반복 알고리즘
def factorial(n): # 필요한 숫자 n을 매개변수로 받음
    the_product = 1 # n 이하의 양의 정수들의 곱을 저장할 the_product 변수를 정의하고 초기값 1
    while n > 0:
        the_product *= n
        n = n - 1
    return the_product

# 2. 숫자 n의 팩토리얼을 계산하는 재귀 알고리즘
def factorial(n):
    if n == 0:  # 종료 조건 정의
        return 1
    return n * factorial(n - 1)