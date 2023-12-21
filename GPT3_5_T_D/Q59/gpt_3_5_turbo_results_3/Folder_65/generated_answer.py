
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[32]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            is_truncatable = True
            digits = str(num)
            for i in range(1, len(digits)):
                truncated_num = int(digits[i:])
                if not is_prime(truncated_num):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)
