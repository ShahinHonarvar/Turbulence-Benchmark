
def all_left_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def is_truncatable_prime(n):
        digits = str(n)
        left_truncated = [int(digits[i:]) for i in range(len(digits))]
        right_truncated = [int(digits[:i+1]) for i in range(len(digits))]
        return all(is_prime(x) for x in left_truncated) and all(is_prime(x) for x in right_truncated)
    
    x = numbers[100]
    truncatable_primes = [i for i in range(2, x+1) if is_prime(i) and is_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)
