
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_prime(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    right_truncatable_primes = []
    for prime in primes:
        is_right_truncatable = True
        digits = list(str(prime))
        for i in range(len(digits)-1):
            digits.pop()
            truncated_num = int(''.join(digits))
            if not is_prime(truncated_num):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(prime)
    return right_truncatable_primes[::-1]

def all_right_truncatable_prime(numbers):
    x = numbers[37]
    return right_truncatable_prime(x)
