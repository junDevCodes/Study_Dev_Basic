# 괄호가 제대로 짝이 맞는 지를 확인하는 함수
def check_match(expression):
    stack = []
    # Key =>닫힌 괄호
    # Value => 열린 괄호
    matching_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # 주어진 입력값을 순회하면서
    for char in expression:
        # 열린괄호 => 스택에 넣는다.
        if char in matching_dict.values():
            stack.append(char)
        # 닫힌괄호 => 스택에서 꺼낸다.
        elif char in matching_dict.keys():

            # 스택이 비어있으면 땡
            if not stack:
                return False

            # 마지막에 들어간 열린 괄호가 닫힌 괄호와 짝이 맞지 않는다면 땡
            if stack[-1] != matching_dict[char]:
                return False

            # 열린 괄호는 짝이 맞으니까 추출만 한다.
            stack.pop()

    # 스택이 비어있지 않으면 떙
    if not stack:
        return False

    # 이친구는 옳은 괄호다
    return True

examples = ["(a(b)", "a(b)c)", "a{b(c[d]e}f)"]
for ex in examples:
    if check_match(ex):
        print(f"{ex} 는 올바른 괄호")
    else:
        print(f"{ex} 는 올바르지 않은 괄호")
