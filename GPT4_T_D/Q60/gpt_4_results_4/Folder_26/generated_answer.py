
def all_left_right_truncatable_prime(nums):
    from sympy import isprime
    
    def is_left_right_truncatable_prime(prime):
        if '0' in str(prime):
            return False
        for i in range(1, len(str(prime))):
            left_trunc = int(str(prime)[i:])
            right_trunc = int(str(prime)[:len(str(prime))-i])
            if not isprime(left_trunc) or not isprime(right_trunc):
                return False
        return True

    trunc_primes = [i for i in range(11, nums[81]) if isprime(i) and is_left_right_truncatable_prime(i)]
    return sorted(trunc_primes, reverse=True)
