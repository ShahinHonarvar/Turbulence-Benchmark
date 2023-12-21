
def all_left_right_truncatable_prime(nums):
    def is_truncatable_prime(num):
        primes = [2, 3, 5, 7]
        if num < 10:
            return num in primes
        else:
            str_num = str(num)
            if str_num[0] == '0' or str_num[-1] == '0':
                return False
            else:
                left_truncatable = is_truncatable_prime(int(str_num[1:]))
                right_truncatable = is_truncatable_prime(int(str_num[:-1]))
                
                return left_truncatable and right_truncatable
    
    result = []
    for num in nums:
        if is_truncatable_prime(num):
            result.append(num)
    
    return sorted(result)
