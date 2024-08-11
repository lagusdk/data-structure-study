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