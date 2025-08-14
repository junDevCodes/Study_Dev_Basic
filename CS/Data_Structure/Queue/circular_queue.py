class CircularQueue:
    def __init__(self, capacity=10):
        # 실제 용량은 어떻게 설정해야 한다고 했었죠 ?
        # 한 칸은 항상 비워둘라고
        self.capacity = capacity + 1
        self.items = [None] * capacity  # 원형큐 리스트 초기화
        self.front = 0  # 원형 큐의 맨 앞 요소를 가리키는 포인터
        self.rear = 0  # 원형 큐의 맨 뒤 요소를 가리키는 포인터

    def is_empty(self):
        # 서로의 포인터의 위치가 같으면 비어있는 거다.
        return self.front == self.rear

    # 원형큐가 가득찼는 지 확인하는 메서드
    def is_full(self):
        # rear의 +1 에 front가 있으면 큐가 가득찬거다 .
        # 논리적 순환을 위해서 % 연산자의 나머지를 이용해준다.
        return (self.rear + 1) % self.capacity == self.front

    # 원형 큐에 데이터를 삽입하는 메서드
    def enqueue(self, item):
        # 삽입하기 전에 가득찼는 지부터 확인해야 한다.
        if self.is_full():
            raise IndexError("가득찼어요 ~ ")
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item

    # 원형 큐에서 데이터를 추출하는 메서드
    def dequeue(self):
        if self.is_empty():
            raise IndexError(" 데이터가 업서용 ~ ")
        self.front = (self.front + 1) % self.capacity
        item = self.items[self.front]
        self.items[self.front] = None
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("값이 엄서용 ")
        return self.items[(self.rear + 1) % self.capacity]

    # 현재 원형 큐에 남아있는 항목의 개수를 반환
    def get_size(self):
        return (self.rear - self.front + self.capacity + 1) % self.capacity


queue = CircularQueue(5)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
