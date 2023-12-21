
def all_right_truncatable_prime(nums):
    from sympy import isprime

    x = nums[46]
    primes = []
  
    def check_right_truncatable(num):
        str_num = str(num)
        len_num = len(str_num)
        for i in range(len_num):
            if not isprime(int(str_num[i:])):
                return False
        return True

    for num in range(2, x):
        if check_right_truncatable(num):
            primes.append(num)

    return sorted(primes, reverse=True)
