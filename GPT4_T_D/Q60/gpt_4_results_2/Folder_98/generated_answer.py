
def all_left_right_truncatable_prime(nums):
    from sympy import isprime

    def is_left_right_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
            if not isprime(int(str_num[:len(str_num)-i])):
                return False
        return True

    x = nums[8]
    lrt_primes = []

    for i in range(2, x+1):
        if is_left_right_truncatable(i):
            lrt_primes.append(i)
    
    lrt_primes.sort(reverse=True)

    return lrt_primes
