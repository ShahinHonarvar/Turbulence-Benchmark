
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if x < 23:
            continue
        truncatable_primes = []
        for num in range(23, x + 1):
            if '0' in str(num):
                continue
            prime = True
            for i in range(1, len(str(num))):
                left_truncation = int(str(num)[i:])
                right_truncation = int(str(num)[:-i])
                if not is_prime(left_truncation) or not is_prime(right_truncation):
                    prime = False
                    break
            if prime:
                truncatable_primes.append(num)
        primes.extend(truncatable_primes)
    return sorted(primes)
