class Node:
    def __init__(self, data):
        self.data = data  # 노드의 데이터
        self.next = None  # 다음 노드를 가리키는 포인터


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # 링크드 리스트의 헤드 초기화

    # 특정 위치에 노드를 삽입하는 메서드
    def insert(self, data, position):
        # 삽입할 새로운 노드 생성
        new_node = Node(data)

        # 맨 앞에 노드를 삽입하는 경우
        if position == 0:
            # 현재 헤드가 가리키고 있는 주소를 새로 생성한 노드의 다음 주소에 저장
            new_node.next = self.head

            # 헤드가 가리키는 주소를 새로 생성한 노드로 변경
            self.head = new_node
            # 맨 앞이 아닌 위치에 삽입하는 경우 (중간, 마지막 )
        else:
            # 삽입할 위치를 찾기 위해서 head부터 시작
            current = self.head

            # 삽입 위치 이전까지 이동
            for _ in range(position - 1):
                if current is None:  # 즉, 마지막 노드가 가리키는 None 주소까지 온 경우
                    print("범위를 벗어난 삽입입니다.")
                    return
                # 삽입하려고 하는 위치까지 반복하면서, 현재 위치(current)를 갱신
                current = current.next

            # 새로운 노드의 다음을 현재 노드의 다음으로 설정
            new_node.next = current.next

            # 현재 노드의 다음을 새로운 노드로 설정
            current.next = new_node

            # 리스트의 끝에 노드를 추가하는 메서드

    # 끝에 추가하는 작업은 자주 일어나므로 기능을 분리해서 구현
    def append(self, data):
        new_node = Node(data)  # 추가할 새로운 노드 생성
        if self.is_empty():  # 리스트가 비어있는 경우
            # 헤드가 새로 생성된 노드를 가리키도록 설정
            self.head = new_node
        # 리스트가 비어있지 않은 경우
        else:
            # 헤드부터 시작해서 마지막 노드를 찾음
            current = self.head
            # while 루프를 벗어났다는 건, current가 마지막 노드를 가리키고 있다는 의미
            while current.next:
                current = current.next
            # 마지막 노드의 다음을 새로운 노드로 설정
            current.next = new_node

    # 리스트가 비어있는지 확인하는 메서드
    def is_empty(self):
        return self.head is None  # 헤드가 None인지 확인

    # 특정 위치의 노드를 삭제하는 메서드
    def delete(self, position):
        if self.is_empty():  # 리스트가 비어있는 경우
            print("싱글 링크드 리스트가 비었습니다.")
            return

        # 첫 번째 노드를 삭제하는 경우
        if position == 0:
            deleted_data = self.head.data  # 삭제할 데이터 저장
            # "헤드가 가리키는 노드"를 "현재 헤드가 가리키고 있는 노드의 다음 노드"로 변경
            self.head = self.head.next

            # 첫 번째 노드가 아닌 위치를 삭제하는 경우
        else:
            # 삭제 위치 전까지 이동
            current = self.head
            for _ in range(position - 1):
                # 삭제할 위치 전까지 이동해야하므로, current.next가 None인 경우도 체크
                if (current is None or current.next is None):
                    print("범위를 벗어났습니다.")
                    return
                current = current.next

            # 삭제할 노드는 현재 노드의 다음 노드
            deleted_node = current.next
            # 삭제할 노드의 데이터를 반환해야 하므로, 데이터 필드에 있는 데이터 저장
            deleted_data = deleted_node.data

            # 현재 노드가 가리킬 포인트를 "현재 노드가 가리키고 있는 다음의 다음"으로 설정
            current.next = current.next.next

        return deleted_data  # 삭제한 데이터 반환

    # 특정 데이터를 가진 노드의 위치를 찾는 메서드
    def search(self, data):
        # 헤드를 시작으로 탐색
        current = self.head
        # 찾은 데이터의 인덱스를 저장할 변수
        position = 0
        # 현재 노드가 None이 아닐 때까지 반복
        # 즉, 리스트의 끝까지 탐색
        while current:
            # 현재 노드의 데이터가 찾고자 하는 데이터와 일치하는 경우, 해당 노드의 위치를 반환
            if current.data == data:
                return position
            # 찾는 노드가 아니라면, 다음 노드로 이동
            current = current.next
            # 이동했기 때문에 현재 노드의 위치도 1을 증가
            position += 1
        # 찾는 데이터가 리스트에 없는 경우, -1을 반환
        return -1

    # 리스트를 문자열로 변환하는 메서드
    def __str__(self):
        result = []
        current = self.head
        while current:  # 리스트를 순회하며 데이터를 결과 리스트에 추가
            result.append(current.data)
            current = current.next
        return str(result)  # 결과 리스트를 문자열로 변환하여 반환


sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
print(sll)  # [1, 2, 3]

deleted_item = sll.delete(1)
print(f"Deleted item: {deleted_item}")  # 2
print(sll)  # [1, 2, 3]
