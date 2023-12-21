
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def truncate_left(n):
        digits = str(n)
        truncated_nums = []
        for i in range(len(digits)):
            truncated_nums.append(int(digits[i:]))
        return truncated_nums
    
    x = numbers[98]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncated_nums = truncate_left(num)
            all_prime = all(is_prime(n) for n in truncated_nums)
            if all_prime:
                truncatable_primes.append(num)
    
    truncatable_primes.sort()
    return truncatable_primes
