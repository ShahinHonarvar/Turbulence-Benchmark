
def all_right_truncatable_prime(numbers):
    x = numbers[429]
    prime_numbers = []
    for i in range(x):
        if is_prime(i) and is_right_truncatable(i, x):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n, x):
    while n > 0 and n not in prime_numbers:
        n = int(str(n)[:-1])
    return n in prime_numbers
