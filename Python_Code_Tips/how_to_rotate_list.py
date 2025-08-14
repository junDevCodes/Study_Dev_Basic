origin_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""
전치(행과 열을 바꿈)
언패킹으로 각 리스트를 추출하고, zip으로 각 열끼리 묶어준다.
"""
reverse_matrix = list(map(list, zip(*origin_matrix)))
"""
90도 시계방향 회전 (행을 뒤집고, 전치)
(i, j) => (j, n-1-i)
2. (n-1-i, j) => 행을 뒤집고
3. (j, n-1-i) => 전치 
"""
rotate_90_clockwise_matrix = list(zip(*origin_matrix[::-1]))
"""
90도 반시계방향 회전 (전치, 행을 뒤집기)
(i, j) => (n-1-j, i)
2. (j, i) => 전치
3. (n-1-j, i) => 행 뒤집기 
"""
rotate_90_counter_clockwise_matrix = list(zip(*origin_matrix))[::-1]
"""
(n-1-i, m-1-j)
각 열에 대해서 뒤집고, 최종적으로 행에 대해서 뒤집기 
"""
rotate_180_matrix = [list(row)[::-1] for row in origin_matrix[::-1]]

print("오리지널")
for i in origin_matrix:
    print(i)

print("전치(행과 열을 바꿈)")
for i in reverse_matrix:
    print(i)

print("90도 시계방향 회전")
for i in rotate_90_clockwise_matrix:
    print(i)

print("90도 반시계방향 회전")
for i in rotate_90_counter_clockwise_matrix:
    print(i)

print("180도 회전")
for i in rotate_180_matrix:
    print(i)

