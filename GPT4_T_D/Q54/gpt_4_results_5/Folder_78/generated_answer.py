
def all_right_truncatable_prime(nums):
    x = nums[23]
    
    def is_prime(num):
        if num == 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[:len(num_str)-i])):
                return False
        return True
    
    truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)
