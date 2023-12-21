
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    x = numbers[758]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            temp = num
            is_truncatable = True
            while temp > 0:
                if not is_prime(temp):
                    is_truncatable = False
                    break
                temp //= 10
            if is_truncatable:
                truncatable_primes.append(num)
    
    return sorted(truncatable_primes)
