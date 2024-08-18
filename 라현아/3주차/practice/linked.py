class Node:
    def __init__(self, data, next=None):
        self.data = data # 변수 data: 데이터를 담음
        self.next = next # 변수 next: 다음 노드를 가리킴

class LinkedList:
    def __init__(self):
        self.head = None # 리스트의 헤드를 나타내는 인스턴스 변수

    def append(self, data): # 클래스 내부에 새로운 노드를 추가할 때 사용하는 append 메서드
        if not self.head: # 리스트에 헤드가 없다면 
            # 새로운 노드를 만들어 헤드로 삼음
            # 매개변수로 데이터를 받아 새로운 노드를 만든 다음, 링크드 리스트에 추가
            self.head = Node(data) 
            return
        # 리스트에 헤드가 있다면
        # 새로운 노드 만들고, 마지막 노드를 찾아 인스턴스 변수 next에 새로운 노드를 할당
        # 이를 위해 current 변수 생성, 리스트 헤드를 할당
        current = self.head 
        while current.next: # while 루프 사용: current.next가 None이 아닌 한 계속 반복해 링크드 리스트의 마지막으로 이동
            current = current.next # current가 None이 될 때까지 current에 current.next를 할당
        current.next = Node(data) # 이제 current 변수가 마지막 노드를 가리킴 -> 새로운 노드를 만들어 current.next에 할당

    def search(self, target): # 탐색하려는 데이터인 target 매개변수
        current = self.head 
        while current.next: 
            if current.data == target: # 링크드 리스트를 거치면서 현재 노드의 데이터와 일치하면 Truee 반환
                return True
            else: # 일치하지 않으면 current에 다음 노드를 할당하고 반복
                current = current.next
        return False # 링크드 리스트의 마지막까지 진행하고도 일치하는 요소를 발견하지 못하면 False 반환
    
    def remove(self, target): # 제거할 노드의 데이터인 target 매개변수
        if self.head == target: # 제거할 노드가 헤드인 경우
            self.head = self.head.next # self.head에 다음 노드를 할당하고 종료
            return
        # 현재 노드와 이전 노드를 각각 변수 current와 previous에 저장
        current = self.head
        previous = None
        while current: # 링크드 리스트 순회
            if current.data == target: # 원하는 데이터 찾으면
                # previous.next에 current.next 할당해 리스트에서 노드 제거
                previous.next = current.next
            previous = current
            current = current.next

    def reverse_list(self): # 역순으로 뒤집기
        # 현재 노드와 이전 노드를 각각 변수 current와 previous에 저장
        current = self.head
        previous = None
        while current:
            next = current.next # next 변수에 current.next 할당
            current.next = previous # current.next에 previous 할당 ==> 포인터 방향 바꾸기 완료
            previous = current
            current = next
        # 현시점에서 current가 None이고, 리스트를 뒤집기 전 마지막 노드가 previous에 할당
        self.head = previous # 리스트 뒤집기 전 마지막 노드를 헤드로 바꾸기

    def detect_cycle(self):
        slow = self.head
        fast = self.fast
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except:
                return False

    def __str__ (self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
        return "end"

# append
a_list = LinkedList()
a_list.append("Tuesday")
a_list.append("Wednesday")

print(a_list)

# search
import random

b_list = LinkedList()

for i in range(0, 20):
    j = random.randint(1, 30)
    b_list.append(j)
    print(j, end= " ")

print(a_list.search(10))
