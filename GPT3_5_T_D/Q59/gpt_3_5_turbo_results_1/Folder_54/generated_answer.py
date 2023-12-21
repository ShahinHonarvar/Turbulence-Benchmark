
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[88]
    left_truncatable_primes = []
    
    def is_left_truncatable_prime(num):
        num_str = str(num)
        for i in range(len(num_str)):
            truncated_num = int(num_str[i:])
            if not is_prime(truncated_num):
                return False
        return True
    
    for i in range(x-1, 0, -1):
        if '0' not in str(i) and is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    
    return left_truncatable_primes
