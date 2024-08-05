import time # 파이썬에 내장된 time 모듈

start = time.time()
for i in range(1, 6): 
    print(i)
end = time.time()
print(end - start)