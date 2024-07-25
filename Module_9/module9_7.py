def is_prime(func):
    def wrapper(a, b, c):
        n = func(a, b, c)
        k = 2
        while k * k <= n and n % k != 0:
            k += 1
        if k * k > n:
            print('Простое')
            return n
        else:
            print('Составное')
            return n

    return wrapper

@is_prime
def sum_three(a: int, b: int, c: int):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)