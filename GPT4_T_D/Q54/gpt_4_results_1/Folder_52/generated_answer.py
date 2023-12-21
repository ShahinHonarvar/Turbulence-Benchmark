
def all_right_truncatable_prime(nums):
    x = nums[52]
    
    def is_right_truncatable_prime(num):
        str_num = str(num)
        while len(str_num) > 1:
            str_num = str_num[:-1]
            if not is_prime(int(str_num)):
                return False
        return True
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num) and is_right_truncatable_prime(num):
            truncatable_primes.append(num)
    
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
