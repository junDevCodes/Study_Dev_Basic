from collections import deque

total_candy = 20  # 총 주어진 마이쮸 개수

# queue = []  # 사람들이 줄 서는 큐
queue = deque()
print(queue)

next_person = 1
# queue에다가 어떤 데이터가 필요한지?
# 누가 받을지(사람 번호)
# 몇 개 받을지(받을 개수)
queue.append((next_person, 1))
last_person = None  # 마지막으로 마이쮸를 받을 사람의 번호를 저장할 변수

while total_candy > 0:
    # 캔디를 나눠주는 로직
    # queue에 있는 애들은 캔디를 받으려고 줄을 선 친구들
    # pop(0)을 이용해서 가장 앞의 데이터를 가져온다.
    # person: 받을 사람의 번호, cnt: 받을 사탕의 개수
    # 언패킹을 이용해서 한 번에 할당
    person, cnt = queue.popleft()

    # 남아있는 캔디의 수가 "사람이 받아가야하는 캔디의 수" 보다 많아야 나눠줄 수 있다.
    if total_candy - cnt <= 0:
        # print("total candy:", total_candy)
        # print("몇개를 가져갈까?", cnt)
        last_person = person
        break

    # 받아야하는 개수만큼 총 캔디에서 차감
    total_candy -= cnt

    # 캔디를 받은 사람은 다시 줄을 선다. 대신 받는 캔디의 수 + 1
    queue.append((person, cnt + 1))


    # 다음 사람의 번호를 1 추가 한다.
    next_person += 1
    # 캔디를 받으면=> 새로운 사람이 다시 줄을 선다. (받는 캔디의 수: 1)
    queue.append((next_person, 1))

print("마지막 마이쮸를 가져간 사람의 번호는: ", last_person)