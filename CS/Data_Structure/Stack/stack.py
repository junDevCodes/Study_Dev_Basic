class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity  # 초기 용량을 설정
        self.items = [None] * capacity  # 저장공간 확보
        # top: 가장 마지막 원소의 위치를 가리킨다.
        self.top = - 1  # 초기에는 데이터가 없으니까, -1로 설정

    # 스택이 가득찼는 지 확인하는 메서드
    def is_full(self):
        # 가장 마지막 원소의 위치가 ... 내가 초기에 설정한 크기 - 1 과 같으면 꽉 찬거다..
        return self.top == self.capacity - 1

    # 스택의 마지막 위치에 데이터를 삽입하는 메서드
    def push(self, item):
        # 삽입하기 전에... 삽입할 공간이 있는 지부터 확인해야 한다.
        if self.is_full():
            raise IndexError("Stack is Full")
        # 가득차지 않았다면, top 위치의 +1 에 데이터를 삽입한다.
        self.top += 1
        self.items[self.top] = item

    def is_empty(self):
        return self.top == -1

    # 스택에서 가장 마지막원소를 빼고, 반환하는 작업
    def pop(self):
        # 비어있는 지 확인
        if self.is_empty():
            raise IndexError("Stack is Empty")
        # 스택 pop 은 데이터를 삭제뿐만 아니라, 반환도 한다.
        item = self.items[self.top]
        # 기존에 들어있던 데이터를 제거해준다.
        self.items[self.top] = None
        # 맨 마지막 원소가 사라졌으니, 그 밑에 있는 친구가 마지막 원소가 된다.
        self.top -= 1
        return item

    # pop 이랑은 다르게, 데이터를 지우는게 아니고 출력만 하는거다... 마지막 원소를
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        return self.items[self.top]


stack = Stack(3)

stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())
