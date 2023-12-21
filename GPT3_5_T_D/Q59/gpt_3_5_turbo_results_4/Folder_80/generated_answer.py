
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[14]
    primes = [str(i) for i in range(2, x) if is_prime(i)]
    result = []
    for prime in primes:
        truncatable = True
        for i in range(len(prime)):
            truncated_num = int(prime[i:])
            if not is_prime(truncated_num):
                truncatable = False
                break
        if truncatable:
            result.append(int(prime))
    return sorted(result, reverse=True)
