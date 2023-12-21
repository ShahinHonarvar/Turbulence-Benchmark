
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    for x in numbers:
        primes = []
        if len(str(x)) < 3:
            continue
        for i in range(2, x):
            if is_prime(i):
                primes.append(i)
        if not primes:
            continue
        for prime in primes[::-1]:
            prime_str = str(prime)
            is_truncatable = True
            for j in range(1, len(prime_str)):
                truncated = int(prime_str[:-j])
                if not is_prime(truncated):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(prime)
    return sorted(result, reverse=True)
