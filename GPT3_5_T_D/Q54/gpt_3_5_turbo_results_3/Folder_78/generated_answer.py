
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    x = numbers[23]
    right_truncatable_primes = []
    for num in range(10, x):
        if is_prime(num):
            truncated_num = num
            while truncated_num > 10:
                truncated_num //= 10
                if not is_prime(truncated_num):
                    break
            else:
                right_truncatable_primes.append(num)
                
    return sorted(right_truncatable_primes)
