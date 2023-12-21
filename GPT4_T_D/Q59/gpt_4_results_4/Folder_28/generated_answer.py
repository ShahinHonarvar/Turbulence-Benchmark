
def all_left_truncatable_prime(nums):
    from sympy import isprime
    
    def is_left_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True

    x = nums[19]
    prime_list = [i for i in range(2, x) if is_left_truncatable(i)]
    prime_list.sort()

    return prime_list
