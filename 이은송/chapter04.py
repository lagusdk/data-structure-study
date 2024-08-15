# 버블 정렬 알고리즘 구현 코드
# def bubble_sort(a_list):
#     list_length = len(a_list) - 1
#     for i in range(list_length):
#         for j in range(list_length):
#             if a_list[j] > a_list[j +1]:
#                 a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
#     return a_list

# 버블 정렬은 알고리즘이 단순
# 두 번 중첩된 for 루프에 의존하므로 알고리즘의 시간 복잡도는 O(n**2)
# 데이터 세트가 클 경우는 비효율적

# 버블 정렬은 안정적임(정렬 기준 이외의 요인 때문에 리스트의 순서가 바뀌지 않음)
# 하지만 잘 쓰지 않음

# 삽입 정렬
# 카드 묶음을 정렬하는 것과 비슷한 정렬 알고리즘
# def insertion_sort(a_list):
#     for i in range(1,len(a_list)):
#         value = a_list[i]
#         while i > 0 and a_list[i - 1] > value:
#             a_list[i] = a_list[i - 1]
#             i = i - 1
#         a_list[i] = value
#     return a_list

# 병합 정렬
# 안정적이고 효육적인 알고리즘

# 하이브리드 정렬 알고리즘
# 문제를 해결하는 데 두 개 이상의 알고리즘을 결합한 알고리즘