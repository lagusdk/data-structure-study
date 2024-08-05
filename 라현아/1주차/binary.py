def binary_search(a_list, n):
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == n:
            return True
        else: 
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False

a_list = [1, 8, 32, 91, 5, 15, 9, 100, 3]
print(binary_search(a_list, 91))