# 후위 표기식 계산 함수
def run_calculator(expr):
    stack = []  # 피연산자를 저장할 스택
    tokens = expr.split()  # 후위 표기식이 공백으로 구분해서 건네줬죠. 그래서 split 분리해서 사용한다.

    for token in tokens:
        # 숫자인 경우 => 스택에 추가한다.
        if token.isnumeric():
            stack.append(int(token))
        # 연산자인 경우
        else:
            # 2개의 값을 꺼낸다..
            op2 = stack.pop()
            op1 = stack.pop()
            # 각 연산즤 종류에 따라서 계산을 한다.
            if token == '+':
                result = op1 + op2
            elif token == '-':
                result = op1 - op2
            elif token == '*':
                result = op1 * op2
            elif token == '/':
                result = op1 / op2
            # 계산 결과는 다시 스택에 집어넣는다.
            stack.append(result)

    # 최종 결과를 반환
    return stack.pop()

# 예시
postfix_expression = "3 2 5 * + 8 4 / -"
result = run_calculator(postfix_expression)
print(result)
