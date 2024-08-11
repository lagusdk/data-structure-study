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