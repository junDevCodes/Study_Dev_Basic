def fibonacci(n):
    # n이 0일 때, 0을 반환
    if n == 0:
        return 0

    # n이 1일 때, 1을 반환
    elif n == 1:
        return 1

    # F(n-1) + F(n-2)를 반환
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10)) # 55
