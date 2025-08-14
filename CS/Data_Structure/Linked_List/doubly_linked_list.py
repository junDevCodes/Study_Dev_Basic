class Node:
    def __init__(self, data):
        self.data = data  # 노드의 데이터
        self.prev = None  # 이전 노드를 가리키는 포인터
        self.next = None  # 다음 노드를 가리키는 포인터


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # 리스트의 첫 번째 노드를 가리키는 포인터
        self.tail = None  # 리스트의 마지막 노드를 가리키는 포인터

    def insert(self, data, position):
        new_node = Node(data)  # 새로운 노드 생성
        if position == 0:
            if self.is_empty():
                self.head = new_node  # 리스트가 비어있으면 head와 tail 모두 새로운 노드를 가리킴
                self.tail = new_node
            else:
                new_node.next = self.head  # 새로운 노드의 next가 현재 head를 가리키도록 설정
                self.head.prev = new_node  # 현재 head의 prev가 새로운 노드를 가리키도록 설정
                self.head = new_node  # head가 새로운 노드를 가리키도록 업데이트

        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    print("범위를 벗어났습니다.")
                    return
                current = current.next

            new_node.next = current.next  # 새로운 노드의 next가 current의 next를 가리키도록 설정
            new_node.prev = current  # 새로운 노드의 prev가 current를 가리키도록 설정

            if current.next:
                current.next.prev = new_node  # current의 next의 prev가 새로운 노드를 가리키도록 설정

            current.next = new_node  # current의 next가 새로운 노드를 가리키도록 설정
            if new_node.next is None:
                self.tail = new_node  # 새로운 노드가 마지막 노드라면 tail 업데이트

    # 끝에 데이터를 추가
    def append(self, data):
        new_node = Node(data)  # 새로운 노드 생성
        # 리스트가 비어있으면
        if self.is_empty():
            #  head와 tail 모두 새로운 노드를 가리킴
            self.head = new_node
            self.tail = new_node
        # 리스트가 비어있지 않으면
        else:
            # 현재 tail의 next가 새로운 노드를 가리키도록 설정
            self.tail.next = new_node

            # 새로운 노드의 prev가 현재 tail을 가리키도록 설정
            new_node.prev = self.tail

            # tail이 새로운 노드를 가리키도록 업데이트
            self.tail = new_node

    def is_empty(self):
        return self.head is None  # 리스트가 비어 있는지 확인

    def delete(self, position):
        if self.is_empty():
            print("더블 링크드 리스트가 비었습니다.")
            return

        if position == 0:
            deleted_data = self.head.data
            self.head = self.head.next  # head를 다음 노드로 업데이트
            if self.head:
                self.head.prev = None  # 새로운 head의 prev를 None으로 설정
            else:
                self.tail = None  # 리스트가 비어있으면 tail도 None으로 설정
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None or current.next is None:
                    print("범위를 벗어났습니다.")
                    return
                current = current.next

            deleted_node = current.next
            deleted_data = deleted_node.data
            current.next = deleted_node.next  # current의 next가 deleted_node의 next를 가리키도록 설정

            if deleted_node.next:
                deleted_node.next.prev = current  # deleted_node의 next의 prev가 current를 가리키도록 설정

            if current.next is None:
                self.tail = current  # 삭제 후 current가 마지막 노드라면 tail 업데이트

        return deleted_data

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position  # 데이터를 찾으면 위치 반환
            current = current.next
            position += 1
        return -1  # 데이터를 찾지 못하면 -1 반환

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)  # 리스트의 모든 노드를 순회하며 데이터를 결과 리스트에 추가
            current = current.next
        return str(result)  # 결과 리스트를 문자열로 변환하여 반환


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
print(dll)  # [1, 2, 3]

deleted_item = dll.delete(1)
print(f"Deleted item: {deleted_item}")  # 2
print(dll)  # [1, 2, 3]
