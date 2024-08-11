# TeaNet 자료구조 STUDY: 2주차(1)

## CHAPTER 05: 문자열 알고리즘

- **애너그램 Anagram**
    - 문자의 순서나 대소에 관계없이 똑같은 문자들로 구성된 문자열
    - 두 문자열이 애너그램인지 판단하는 것의 핵심 → 정렬
        - 정렬된 문자열이 일치 → 두 문자열은 애너그램
        
        ```python
        def is_anagram(s1, s2):
            s1 = s1.replace(' ', '').lower() # 문자열에서 공백을 모두 제거하고 소문자로 통일
            s2 = s2.replace(' ', '').lower()
            if sorted(s1) == sorted(s2): # 파이썬의 sorted 함수 사용 -> 시간 복잡도 O(n log n)
                return True
            else:
                return False
        
        s1 = 'Emperor Octavian'
        s2 = 'Captain over Rome'
        print(is_anagram(s1, s2))
        ```
        
- **팰린드롬(회문) Palindrome**
    - 앞에서 읽으나 거꾸로 읽으나 똑같은 단어
    - 문자열을 복사해 순서를 뒤집은 다음(`print("blackswan"[::-1])`) 원래 문자열과 비교
        - 두 문자열이 일치하면 팰린드롬
        
        ```python
        def is_palindrome(s1):
            if s1.lower() == s1[::-1].lower(): # 요소 전체를 하나씩 비교 -> 시간 복잡도 O(n)
                return True
            return False
        ```
        
- **리스트 축약 문법 List Comprehension** → 문자열의 가장 오른쪽에 있는 숫자 찾기
    - 원래의 이터러블 리스트에서 새로운 리스트를 만드는 파이썬 문법
        - `new_list = [expression(i) for i in iterable if filter(i)]`
            - `iterable` 새로운 리스트를 만들기 위한 재료
            - `expression(i)` iterable의 각 요소를 저장할 변수
        
        ```python
        print([c for c in "selftaught"] ) # 모든 문자를 포함하는 리스트 반환
        print([c for c in "selftaught" if ord(c) > 102] ) # ASCII 코드가 102보다 큰 문자 = f 다음 글자만 남김
        
        s = "Buy 1 get 2 free"
        nl = [c for c in s if c.isdigit()][- 1] # 내장 함수 isdigit(숫자만) & 마이너스 인덱스(리스트의 마지막) -> 시간 복잡도 O(n) 
        print(nl)
        ```
        
    - 연습문제 파이썬의 리스트 축약 문법을 사용해 다음의 리스트에서 다섯 글자 이상인 단어만 반환
        
        ["selftaught", "code", "sit", "eat", "programming", "dinner", "one", "two", "coding", "a", "tech"]
        
        ```python
        list = ["selftaught", "code", "sit", "eat", "programming", "dinner", "one", "two", "coding", "a", "tech"]
        test = [c for c in list if len(c) >= 5]
        print(test)
        ```
        
- **암호 Cipher**
    - 암호화나 복호화에 사용되는 알고리즘
    - 시저의 암호
        - 하나의 숫자를 선택하고 메시지의 모든 문자를 그 숫자만큼 이동시켜 새로운 메시지를 만드는 것
        - 숫자를 더한 문자의 위치가 알파벳의 범위를 넘어가면 다시 처음 알파벳으로 돌아옴
        - 핵심: 나머지 연산
    
    ```python
    import string
    
    def chpher(a_string, key):
        uppercase = string.ascii_uppercase # 대문자 알파벳 문자열
        lowercase = string.ascii_lowercase # 소문자 알파벳 문자열
        encrypt = '' # 빈 문자열 -> 암호화된 문자열
        for c in a_string: # 시간 복잡도 O(n)
            if c in uppercase:
                new = (uppercase.index(c) + key) % 26
                encrypt += uppercase[new]
            elif c in lowercase:
                new = (lowercase.index(c) + key) % 26
                encrypt += lowercase[new]
            else:
                encrypt += c
        return encrypt
    ```
    

## CHAPTER 06: 수학

- **이진수 Binary Number**: 이진법에서 쓰는 숫자
    - 파이썬 `bin()` 함수
- **진법 Numeral System**: 숫자를 표현하고 저장하는 규칙
    - **밑수 Base**: 그 진법에서 사용하는 숫자의 개수
    - **자릿값 Place Value**
        - 여러 개로 구성된 숫자의 위치를 나타내는 개념
    
    ---
    
    - 이진법
        - 이진법의 숫자 **비트 Bit**(=Binary Digit)
            - 0과 1, 단 2개의 숫자(Base=2)
        - 숫자 앞에 b를 써서 이진수임을 나타냄
    - 십진법
        - 0부터 9까지 10개의 숫자(Base=10)
        - 십진법에서 각 자릿값⇒ 모두 10의 거듭제곱
    - **16진법 Hexadecimal System**
- **비트 연산자 Bitwise Operator**
    - 2개의 이진수로 이루어진 표현식에 사용하는 연산자
        - 파이썬의 비트 연산자
            - 비트 단위로 논리 연산(Boolean Arithmetic) 수행
            - AND `print(2 & 3)`
                - 두 비트가 모두 1(`True`)이면 1을 반환, 그렇지 않으면 0(`False`)를 반환
            - OR `print(2 | 3)`
                - 두 비트가 모두 `False`면 `False`를, 그렇지 않으면 `True` 반환
    - 주어진 숫자가 짝수인지 홀수인지 판단
        - 짝수는 0으로 끝나고, 홀수는 1로 끝남
        
        ```python
        def is_even(n):
            return not n & 1 # 홀수 -> True
        ```
        
    - 어떤 정수가 2의 거듭제곱인지 판단
        - 2의 거듭제곱이면 1은 단 하나만 존재하고 나머지는 전부 0
        - 2의 거듭제곱에서 1을 뺀 숫자는 모든 비트가 1
        
        ```python
        def is_power(n):
            if n & (n - 1) == 0:
                return True # 거듭제곱 -> True
            return False
        ```
        
- 피즈버즈
    - 1부터 100까지의 숫자를 출력하는 프로그램
        - 숫자가 3의 배수 → 숫자 대신 Fizz 출력
        - 숫자가 5의 배수 → 숫자 대신 Buzz 출력
        - 숫자가 3과 5의 공배수 → 숫자 대신 FizzBuzz 출력
    - 핵심: 나머지 연산자
    
    ```python
    def fizzbuzz(n):
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print('FizzBuzz')
            elif i % 3 == 0:
                print('Fizz')
            elif i % 5 == 0:
                print('Buzz')
            else:
                print(i)
    ```
    
- **최대공약수 Greatest Common Factor**
    - **경계 조건 Boundary Condition**
        - 코드가 0을 제대로 처리하지 못하는 경우
        - 개발자가 프로그램에 입력할 것이라고 예상하지 못했던 값
        
        ```python
        def gcf(i1, i2): # n에 정비례 -> 선형 시간 복잡도
            if i1 < 0 or i2 < 0:
                raise ValueError("Numbers must be positive,")
            if i1 == 0:
                return i2
            if i2 == 0:
                return i1
            
            if i1 > i2:
                smaller = i2
            else:
                smaller = i1
        
            for divisor in range(1, smaller + 1):
                if (i1 % divisor == 0) and (i2 % divisor == 0):
                    gcf = divisor
                return gcf
        ```
        
    - **유클리드 알고리즘 Euclid’s Algorithm**
        - 숫자 x를 다른 숫자 y로 나눈 나머지 구함
            - 나머지를 y, 이전 단계의 y를 x로 놓고 다시 나눔
                - 나머지가 0이 될 때까지 반복
                    - 나머지가 0이 될 때 나눈 수 = 최대공약수
        
        ```python
        def gcf(x, y): # 로그 시간 복잡도
            if y == 0: # 경계 조건
                x, y = y, x
            while y != 0:
                x, y = y, x%y
            return x
        ```
        
- **소수 Prime Number**
    - 자기 자신과 1로만 나누어 떨어지는 양의 정수
    
    ```python
    import math
    
    def is_prime(n): # 선형 알고리즘
        for i in range(2, int(math.sqrt(n))+1): # n의 제곱근에서 루프 종료
            if n % 1 == 0:
                return False
            return True
        
    def find_primes(n): # 시간 복잡도 O(n**2)
        return [i for i in range(2, n) if is_prime(i)]
    ```