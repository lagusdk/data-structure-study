class Stack:
    def __init__(self):
        self.items = [] # 인스턴스 변수 items를 정의, 비어 있는 리스트로 초기화

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop() # 가장 최근에 추가된 요소 반환 메서드 pop
    
    def size(self):
        return len(self.items) # 스택 길이 반환
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        return self.items[-1]