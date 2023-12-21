
import sympy

def all_left_truncatable_prime(nums):
    x = nums[8]
    result = []
   
    for i in range(2, x):
        if not sympy.isprime(i):
            continue
        if '0' in str(i):
            continue
        length = len(str(i))
        left_truncatable = True
        for j in range(1, length):
            if not sympy.isprime(int(str(i)[j:])):
                left_truncatable = False
                break
        if left_truncatable:
            result.append(i)
    return sorted(result, reverse=True)
