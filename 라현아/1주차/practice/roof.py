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
