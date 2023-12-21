
import sympy

def all_right_truncatable_prime(nums):
    if len(nums) < 31:
        return []
    max_number = nums[30]
    right_truncatable_primes = []
    for num in range(max_number, 2, -1):
        str_num = str(num)
        flag = 0
        if sympy.isprime(num):
            for i in range(len(str_num)):
                if not sympy.isprime(int(str_num[0:len(str_num)-i])):
                    flag = 1
                    break
            if flag == 0:
                right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
