
def all_left_right_truncatable_prime(nums):
    from sympy import isprime

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not isprime(int(str(n)[i:])) or not isprime(int(str(n)[:len(str(n))-i])):
                return False
        return True

    x = nums[52]
    return sorted([num for num in range(10, x+1) if is_left_right_truncatable_prime(num)], reverse=True)
