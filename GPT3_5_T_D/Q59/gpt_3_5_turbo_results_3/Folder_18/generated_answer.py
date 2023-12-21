
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[429]
    truncatable_primes = []
    for i in range(10, x):
        if '0' not in str(i):
            truncatable_prime = True
            digits = str(i)
            for j in range(len(digits)):
                truncated_num = int(digits[j:])
                if not is_prime(truncated_num):
                    truncatable_prime = False
                    break
            if truncatable_prime:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)
