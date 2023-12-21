
def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[55]
    primes = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        truncated_number = str(i)
        is_left_truncatable_prime = True
        while truncated_number != '':
            if not is_prime(int(truncated_number)):
                is_left_truncatable_prime = False
                break
            truncated_number = truncated_number[1:]
        if is_left_truncatable_prime:
            primes.append(i)
    return sorted(primes)
