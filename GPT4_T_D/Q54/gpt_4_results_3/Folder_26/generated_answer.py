
def all_right_truncatable_prime(nums):
    from sympy import isprime
  
    # function to check if a number is right-truncated prime
    def is_right_truncatable_prime(num):
        while num > 0:
            if not isprime(num):
                return False
            num //= 10
        return True

    x = nums[81]
    right_truncatable_primes = [num for num in range(x) if is_right_truncatable_prime(num)]
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
