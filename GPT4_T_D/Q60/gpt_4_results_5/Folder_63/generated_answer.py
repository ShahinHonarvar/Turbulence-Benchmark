
def all_left_right_truncatable_prime(nums):
    from sympy import isprime
    x = nums[88]
    def is_truncatable(n):
        if '0' in str(n): return False
        return all(isprime(int(str(n)[i:])) and isprime(int(str(n)[:i+1])) for i in range(len(str(n))))
    return sorted([i for i in range(10, x+1) if isprime(i) and is_truncatable(i)])
