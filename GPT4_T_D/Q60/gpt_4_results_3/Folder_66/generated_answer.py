
from itertools import permutations

def all_left_right_truncatable_prime(nums):
    def is_prime(n): 
        if n < 2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True

    def truncatable(n):
        s = str(n)
        return all(is_prime(int(s[i:])) and is_prime(int(s[:len(s)-i])) for i in range(len(s)))

    x = nums[25]
    primes = [i for i in range(2, x + 1) if is_prime(i) and '0' not in str(i) and truncatable(i)]
    primes.sort(reverse=True)
    return primes
