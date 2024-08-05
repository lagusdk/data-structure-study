# TeaNet 자료구조 STUDY: 1주차

## 📚나의 첫 알고리즘+자료구조 with 파이썬

> PART 01 알고리즘
> 

### CHAPTER 01 알고리즘이란?

- **알고리즘 Algorithm**
    - 어떤 문제를 해결하기 위해 밟아 나가는 연속적인 단계
    - 도널드 커누스曰
        - 입력을 기반으로 출력을 생성하는
        - 명확하고 효율적이며 유한한 프로세스
            - **명확함 Definiteness**: 각 단계가 명료하고 간결하며 모호하지 X
            - **효율성 Effectiveness**: 각 동작이 문제 해결에 기여
            - **유한함 Finiteness**: 알고리즘이 유한한 단계를 거친 후 종료
            - +) **정확성 Correctness**: 입력이 같으면 항상 같은 결과
- 알고리즘 평가 기준
    - **실행 시간**
        - 변수
            - 컴퓨터 CPU 자원
                - 프로그램 실행 → 컴퓨터가 사용 가능한 CPU 자원이 매번 다름
                    
                    ⇒ 프로그램 실행시간에 영향 → 알고리즘 실행시간에도 영향
                    
            - 프로그래밍 언어
- 알고리즘의 단계 f(n)
    - **데이터의 크기** 변수 n
        - f(n) = 1 + 2n ⇒ 문제해결 필요시간 T(n) = 1 + 2n
            
            ```python
            count = 0
            for i in range(1, n): 
                print(i)
                count += i
            # count 할당 + 출력 n번 + 출력된 숫자 합 계산 n번
            # f(n) = 1 + 2n
            ```
            
        - **n의 변화에 따른 알고리즘 성능의 변화 예상**
            - for 함수가 두 번 중첩된 루프를 n번 반복 ⇒ n**2
                
                ```python
                def print_it(n):
                    # 루프 1 
                    # T(n) = n
                    for i in range(n):
                        print(i)
                    # 루프 2
                    # T(n) = n**3
                    for i in range(n):
                        print(i)
                        for j in range(n):
                            print(j)
                            for h in range(n):
                                print(h)
                ```
                
            - *“n이 커질 때 알고리즘의 단계가 얼마만큼 증가하는가” ⇒ **빅 O 표기법 Big O notation***
                - n이 커짐에 따라 알고리즘의 시간 or 공간의 요건이 얼마나 커지는지 나타내는 수학적 표기법
                - T(n)에서 규모 함수 도출
                    - **규모 Order of Magnitude**: 차이가 아주 큰 등급 체계에서의 크기 차이
                    - T(n)에서 가장 지배적인 부분 = 빅 O 표기법에서 도출한 알고리즘의 규모
                    - **시간 복잡도 Time Complexity**: n이 커짐에 따라 알고리즘이 실행되고 완료될 때까지 필요한 단계
                        - `효율적` 상수 시간 → 로그 시간 → 선형 시간 
                        → 선형 로그 시간 → 2차 시간 → 3차 시간 → 지수 시간 `비효율적`
                        - **상수 시간 복잡도 Constant — O(1)**
                            - 어떤 알고리즘이 n의 크기에 관계없이 동일한 단계만 필요한 경우
                                
                                ```python
                                free_books = customers[0]
                                # T(n) = 1
                                ```
                                
                            - ‘알고리즘이 **상수 시간**으로 실행된다’
                            - 데이터 세트가 아무리 커지더라도 알고리즘의 실행 시간이 변하지 X
                        - **로그 시간 복잡도 Logarithmic — O(log n)**
                            - 데이터 로그에 비례해 알고리즘 단계가 늘어날 경우
                            - 실행을 반복할 때마다 알고리즘의 탐색 범위를 1/2로 줄여 나가는 *이진 탐색*과 같은 알고리즘에서…
                        - **선형 시간 복잡도 Linear — O(n)**
                            - 데이터의 크기가 커지는 만큼 같은 비율로 단계가 늘어나는 경우
                                
                                ```python
                                free_book = False
                                customers = ["Lexi", "Britney", "Danny", "Bobbi", "Chris"]
                                for customer in customers:
                                	if customer[0] == 'B':
                                		print(customer)
                                # f(n) = 1 + 1 + n
                                # O(n) = n
                                ```
                                
                        - **선형 로그 시간 복잡도 Log-Linear — O(n log n)**
                            - 데이터 세트를 작은 부분으로 나누고, 이들을 독립적으로 처리
                            - *병합 정렬*과 같은 효율적인 정렬 알고리즘에서…
                        - **다향 시간 복잡도 Polynomial — O(n**a)**
                            - **2차 시간 복잡도 Quadratic — O(n**2)**
                                - n의 제곱에 정비례
                                    
                                    ```python
                                    numbers = [1, 2, 3, 4, 5]
                                    for i in numbers:
                                    	for j in numbers:
                                    		x = i * j
                                    		print(x)
                                    # f(n) = 1 + n * n * (1 + 1) = 1 + 2 * n**2 
                                    # O(n) = n**2
                                    ```
                                    
                                - *삽입 정렬*이나 *버블 정렬*과 같은 정렬 알고리즘의 상당수에서…
                            - **3차 시간 복잡도 Cubic — O(n**3)**
                                
                                ```python
                                numbers = [1, 2, 3, 4, 5]
                                for i in numbers:
                                	for j in numbers:
                                		for h in numbers:
                                			x = i + j + h 
                                			print(x)
                                # f(n) = 1 + n * n * n * (1 + 1) = 1 + 2 * n**3
                                # O(n) = n**3
                                ```
                                
                        - **지수 시간 복잡도 Exponential — O(c**n)**
                            - **무차별 대입 알고리즘 Brute-Force Algorithm**
                                - 가능한 경우의 수를 전부 대입
                    
                    ---
                    
                    - **Best-case**: 알고리즘에 입력되는 데이터가 이상적일 경우
                    - **Worst-case**: 알고리즘의 실행 시간이 급격하게 커지는/느려지는 경우
                    - **Average-vase**: 알고리즘이 평균적으로 얼마나 빨리 실행되는지
                    
                    ---
                    
                    - **공간 복잡도 Space Complexity**: 알고리즘이 실행을 완료할 때까지 필요한 자원의 양, 즉 고정 공간, 데이터 구조 공간, 임시 공간의 메모리를 얼마나 사용하는지
                        - **고정 공간 Fixed —** : 프로그램 자체가 차지하는 메모리
                        - **자료구조 공간 Data Structure —** : 데이터 세트를 저장하는 데 필요한 메모리
                        - **임시 공간 Temporary —** : 알고리즘에서 중간 처리를 위해 사용하는 메모리

### CHAPTER 02 재귀

- **반복 알고리즘 Iterative Algorithm**
    - 동일한 루프로 단계를 반복해 문제를 해결하는 알고리즘
- **재귀 Recursion**
    - 문제를 더 작은 부분으로 나누고, 각 부분의 문제를 해결한 후 결과를 조합해 전체 문제의 답을 찾는 문제 해결 방법
        - 자기 자신을 호출하는 함수나 메서드 사용
        - 함수: 입력을 변경하고 자신을 호출하면서 그 결과를 전달
        - **종료 조건 Base Case 必**
            - 반드시 종료 조건이 있어야 한다.
            - 반드시 자기 자신의 상태를 변경하면서 종료 조건에 가까워져야 한다.
            - 반드시 자기 자신을 재귀적으로(다시 돌아와) 호출해야 한다.

### CHAPTER 03 탐색 알고리즘

- **탐색 알고리즘 Search Algorithm**
    - **선형 탐색 Linear Search** = 순차 탐색 Sequential Search
        - 시간 복잡도 O(n), 최선의 경우 O(1)
    - **이진 탐색 Binary Search**
        - 시간 복잡도 O(log n)
        - 데이터가 많을수록 선형 탐색보다 효율적
- 문자 인코딩
    - ASCII
        - 각각의 글자를 7비트 이진수와 연결 → 최대 128개의 문자 표현 가능
        - but, 대부분의 컴퓨터에서는 8비트로 확장 → 256개의 문자 표현
    - **UTF-8**
        - 32비트 → 100만개

### CHAPTER 04 정렬 알고리즘

- **데이터 정렬 Sorting Data**: 데이터를 일정한 순서로 배치
    - **버블 정렬 Bubble Sort**
        - 숫자 리스트를 순회하면서 각 숫자를 다음 숫자와 비교
        - 순서가 올바르지 않으면 둘의 위치를 바꾸는 정렬 알고리즘
        - 시간 복잡도 O(n**2)
    - **삽입 정렬 Insertion Sort**
        - 시간 복잡도 O(n**2)
    - **하이브리드 정렬 알고리즘 Hybrid Sorting Algorithm**
        - = 버블 정렬 + 삽입 정렬
        - 문제를 해결하는 데 2개 이상의 알고리즘을 결합하여 적용하는 알고리즘
- **분할 정복 알고리즘 Divide-and-Conquer Algorithm**
    - **병합 정렬 Merge Sort**
        - 리스트를 계속해서 반으로 나눠 요소가 한 개 뿐인 리스트로 남았을 때,
            
            이들을 올바른 순서로 다시 합치는 재귀 정렬 알고리즘
            
        - 시간 복잡도 O(n log n)