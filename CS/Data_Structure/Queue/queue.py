class Queue:
    # 생성자 메서드
    # 인스턴스가 생성될 때, 무조건 실행되는 메서드
    # 초기화하는 용도로 사용된다.
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = [None] * capacity  # 초기화한 크기대로 리스트를 설정
        self.front = -1  # 큐의 맨 앞의 요소를 가리키는 인덱스
        self.rear = -1  # 큐의 맨 뒤의 요소를 가리키는 인덱스

    # 큐가 비어있는 지 확인하는 메서드
    def is_empty(self):
        return self.front == self.rear

    # 큐가 가득찼는지 확인하는 메서드
    def is_full(self):
        # 맨 뒤를 가리키는 rear 포인터를 활용해서 확인한다.
        return self.rear == self.capacity - 1

    # 큐에 데이터를 삽입하는 메서드
    def enqueue(self, item):
        # 큐가 가득 찼는지부터 확인해야 한다.
        if self.is_full():
            raise IndexError("큐가 가득참!")

        # rear의 다음 칸에 데이터를 집어넣고, 그 다음에 rear 의 위치를 +1 한다.
        self.rear += 1
        # self.rear = self.rear + 1
        self.items[self.rear] = item

    # 큐에서 데이터를 꺼내는 메서드
    def dequeue(self):
        # 비어있는 지 먼저 확인해야 한다.
        if self.is_empty():
            raise IndexError("큐가 비어있음!")
        # front 포인터 다음 위치의 데이터를 꺼내야 한다.
        self.front += 1
        item = self.items[self.front]
        self.items[self.front] = None  # None으로 초기화를 해주잖아요.. 사실 안해줘도 됩니다.
        return item

    # 맨 앞의 요소만 가져오는 것
    def peek(self):
        if self.is_empty():
            raise IndexError(" 비어있음!")
        return self.items[self.front + 1]

    # 현재 큐에 들어있는 데이터의 개수
    def get_size(self):
        return self.rear - self.front


queue = Queue(5)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Dequeued:", queue.dequeue())  # 1
print("Dequeued:", queue.dequeue())  # 2
