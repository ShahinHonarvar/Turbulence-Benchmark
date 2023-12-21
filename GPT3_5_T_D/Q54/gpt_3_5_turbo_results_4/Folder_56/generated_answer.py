
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) < 31:
        return []
    x = numbers[30]
    truncatable_primes = []
    for i in range(10, x):
        if is_prime(i):
            num = str(i)
            is_truncatable_prime = True
            while len(num) > 1:
                num = num[:-1]
                if not is_prime(int(num)):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                truncatable_primes.append(i)
    return sorted(truncatable_primes)
