# x => 밑
# n => 지수
# x^n
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)


def power2(a, n):
    if n == 0:
        return 1

    x = power2(a, n // 2)

    if n % 2 == 0:  # 짝수일 경우
        return x * x
    else:
        return a * x * x





print(power(2, 10))
print(power(3, 3))
