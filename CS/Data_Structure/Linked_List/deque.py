from collections import deque

queue = deque()
print(queue)
queue.append(1)  # enqueue()
print(queue)
queue.append(2)
print(queue)
queue.appendleft(3)
print(queue)
pop_data = queue.popleft()  # deque()
print(queue, pop_data)
