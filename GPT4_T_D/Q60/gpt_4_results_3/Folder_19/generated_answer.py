
import sympy

def all_left_right_truncatable_prime(nums):
    x = nums[67]

    def left_right_truncatable_prime(n):
        if '0' in str(n): return False
        n = str(n)
        for i in range(len(n)):
            if not (sympy.isprime(int(n[i:])) and sympy.isprime(int(n[:len(n)-i]))):
                return False
        return True

    return sorted([i for i in range(11, x+1) if left_right_truncatable_prime(i)], reverse=True)
