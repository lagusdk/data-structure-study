import math

def is_prime(n): # 선형 알고리즘
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근에서 루프 종료
        if n % 1 == 0:
            return False
        return True
    
def find_primes(n): # 시간 복잡도 O(n**2)
    return [i for i in range(2, n) if is_prime(i)]