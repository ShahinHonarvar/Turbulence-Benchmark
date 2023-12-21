
def all_left_right_truncatable_prime(nums):
    x = nums[86]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:len(str(n))-i])):
                return False
        return True

    truncatable_primes = []
    for i in range(11, x+1):
        if is_left_right_truncatable(i):
            truncatable_primes.append(i)
    
    return truncatable_primes
