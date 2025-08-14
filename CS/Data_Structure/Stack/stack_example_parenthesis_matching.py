# 괄호가 제대로 짝이 맞는 지를 확인하는 함수
def check_match(expression):
    # 짝이 맞는 지를 볼 때는 어떤 자료구조를 쓴다고 했어요 ?
    # Stack => 후입 선출
    stack = []  # 빈 리스트로 초기화
    # key => 닫힌 괄호
    # value => 열린 괄호
    # key 로 접근하면, 그거에 매칭되어야 할 value를 반환해준다.
    matching_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # 주어진 문자열(expression)을 순회하면서, 괄호의 종류에 따라 push, pop을 진행하면서 비교
    for char in expression:
        # 여는 괄호가 나오면, 바로 스택에 넣는다.
        if char in matching_dict.values():
            stack.append(char)
        # 닫힌 괄호가 나오면, 스택에 pop 하고 같은 괄호인 지 비교한다.
        elif char in matching_dict.keys():
            # 스택에서 꺼낸다....! 그리고 비교한다..!
            # 스택이 비어있으면 끝낸다.
            if not stack:
                return False

            # 비어있지 않으니까 꺼냈어요.
            # 짝이 맞는지 확인해야한다.
            # 현재 여기서 char는 닫힌 괄호에요 => key 값으로 넣으면
            # => 이 닫힌 괄호에 매칭되어야 하는 여는 괄호가 나옵니다.
            if stack[-1] != matching_dict[char]:
                return False

            # 스택이 비어있지도 않고,짝도 맞는 경우
            stack.pop()

    if not stack:  # 스택이 안 비었어? 그러면 .. 열린 괄호가 짝이 없다는 소리에요
        return False

    return True

examples = ["(a(b)", "a(b)c)", "a{b(c[d]e}f)"]
for ex in examples:
    if check_match(ex):
        print(f"{ex} 는 올바른 괄호")
    else:
        print(f"{ex} 는 올바르지 않은 괄호")
