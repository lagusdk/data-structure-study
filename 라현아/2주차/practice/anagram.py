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