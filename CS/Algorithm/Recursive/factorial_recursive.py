def factorial(n):
    # n이 1 이하인 경우 1을 반환
    if n <= 1:
        return 1
    else:
        # (n-1)로 자기 자신을 호출
        return n * factorial(n - 1)

print(factorial(5))  # 120
