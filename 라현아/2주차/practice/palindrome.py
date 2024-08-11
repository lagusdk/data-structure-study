print("blackswan"[::-1])

def is_palindrome(s1):
    if s1.lower() == s1[::-1].lower(): # 요소 전체를 하나씩 비교 -> 시간 복잡도 O(n)
        return True
    return False