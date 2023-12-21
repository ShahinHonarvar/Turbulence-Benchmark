
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[33]
    right_truncatable_primes = []
    
    def right_truncate(n):
        truncated = []
        digits = str(n)
        for i in range(len(digits), 0, -1):
            truncated.append(int(digits[:i]))
        return truncated

    for num in range(2, x):
        if is_prime(num):
            truncated = right_truncate(num)
            if all(is_prime(n) for n in truncated):
                right_truncatable_primes.append(num)

    return sorted(right_truncatable_primes)
