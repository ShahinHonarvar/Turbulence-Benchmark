
def all_right_truncatable_prime(numbers):
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
    
    x = numbers[33]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncated = str(num)
            while truncated:
                truncated = truncated[:-1]
                if truncated and not is_prime(int(truncated)):
                    break
            else:
                right_truncatable_primes.append(num)
    
    return sorted(right_truncatable_primes)
