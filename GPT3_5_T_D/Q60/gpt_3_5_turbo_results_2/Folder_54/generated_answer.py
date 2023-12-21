
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[88]
    primes = []
    
    for num in range(2, x + 1):
        str_num = str(num)
        
        if '0' in str_num:
            continue
        
        if is_prime(num):
            left_truncatable = True
            right_truncatable = True
            
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])):
                    right_truncatable = False
                    break
            
            if right_truncatable:
                for i in range(len(str_num)-1, 0, -1):
                    if not is_prime(int(str_num[:i])):
                        left_truncatable = False
                        break
            
            if left_truncatable and right_truncatable:
                primes.append(num)
    
    return sorted(primes, reverse=True)
