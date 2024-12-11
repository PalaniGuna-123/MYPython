def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(3))


def fact(n):
    if n==0:
        return 1
    return n * (n-1)
print(fact(3))