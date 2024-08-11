def is_even(n):
    return not n & 1 # 홀수 -> True

def is_power(n):
    if n & (n - 1) == 0:
        return True # 거듭제곱 -> True
    return False