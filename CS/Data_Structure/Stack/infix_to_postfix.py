# 중위 표기식을 후위 표기식으로 변환하는 함수
def infix_to_postfix(expression):
    # 연산자의 우선순위
    op_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []  # 연산자를 저장할 스택
    postfix = []  # 후위 표기식을 저장할 리스트

    # 주어진 입력값을 하나하나씩 순회하면서 봅시다.
    for ch in expression:
        # 숫자인 경우  => 무조건 후위표기식에 바로 추가한다.
        if ch.isnumeric():
            postfix.append(ch)

        # 여는 괄호인 경우 => 무조건 스택에 넣는다.
        # 계산 영역의 시작이기 때문에, 스택에서 새로운 영역을 만들어야 해요
        elif ch == '(':
            stack.append(ch)

        # 닫힌 괄호인 경우 => 여는 괄호를 만날 때까지 스택에서 연산자를 빼서 출력한다.
        elif ch == ')':
            top_token = stack.pop()  # 스택에서 가장 마지막 연산자를 꺼낸다.
            # 꺼낸 친구가 닫힌 괄호가 아니라면,,, 아래 로직을 계속해서 반복한다.
            # 열린 괄호는 결과에 추가하지 않는다...
            while top_token != '(':
                postfix.append(top_token)  # 여는 괄호가 아니기 때문에 결과에 추가한다.
                top_token = stack.pop()  # 다시 마지막 연산자를 스택에서 꺼낸다.
        # 연산자인 경우
        else:
            """ op_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0} """
            # 스택에 연산자가 들어있는 경우에 그 연산자와 우선순위를 비교해야 한다.
            # "집어넣으려고 하는 연산자" 보다 "스택의 연산자"의 우선순위가 같거나 높으면 => 스택에서 꺼내서 결과에 추가해줘야 한다.
            # "집어넣으려고 하는 연산자" 의 우선순위가 "스택의 연산자"보다 우선순위가 높으면 => 그대로 스택에 집어넣으면 된다.
            # Stack 비어있을 경우 => 바로 스택에 추가한다.
            while stack and op_dict[stack[-1]] >= op_dict[ch]:
                postfix.append(stack.pop())
            stack.append(ch)

    # 만약에 스택에 연산자가 남아 있따면 .. .
    # 스택에 있는 연산자를 모두 꺼내서, 결과에 추가한다.
    while stack:
        postfix.append(stack.pop())

    # 리스트를 문자열로 변환하여 반환, ' ' 공백 간격으로
    return ' '.join(postfix)

infix_expression = "3+(2*5)-8/4"
postfix_expression = infix_to_postfix(infix_expression)
print(f"후위 표기식: {postfix_expression}")
