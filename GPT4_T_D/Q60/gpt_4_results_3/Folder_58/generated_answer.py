
def all_left_right_truncatable_prime(nums):
    x = nums[975]
    truncatable_primes = []
  
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        str_num = str(n)
        if '0' in str_num:
            return False
        
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:len(str_num) - i])):
                return False
        return True

    for num in range(10, x + 1):
        if is_prime(num) and is_left_right_truncatable(num):
            truncatable_primes.append(num)

    return sorted(truncatable_primes, reverse=True)
