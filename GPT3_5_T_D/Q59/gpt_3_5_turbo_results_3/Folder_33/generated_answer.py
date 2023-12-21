
def all_left_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_left_truncatable_prime(n):
        curr_num = n
        while curr_num > 0:
            if not is_prime(curr_num):
                return False
            curr_num = int(str(curr_num)[1:])
        return True
    
    x = nums[945]
    left_truncatable_primes = []
    
    for num in range(2, x):
        if is_prime(num) and '0' not in str(num) and is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    
    return sorted(left_truncatable_primes, reverse=True)
