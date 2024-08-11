def gcf(x, y): # 로그 시간 복잡도
    if y == 0: # 경계 조건
        x, y = y, x
    while y != 0:
        x, y = y, x%y
    return x