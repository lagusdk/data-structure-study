print([c for c in "selftaught"] ) # 모든 문자를 포함하는 리스트 반환
print([c for c in "selftaught" if ord(c) > 102] ) # ASCII 코드가 102보다 큰 문자 = f 다음 글자만 남김

s = "Buy 1 get 2 free"
nl = [c for c in s if c.isdigit()][- 1] # 내장 함수 isdigit(숫자만) & 마이너스 인덱스(리스트의 마지막) -> 시간 복잡도 O(n) 
print(nl)