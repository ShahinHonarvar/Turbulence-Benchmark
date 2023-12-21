
def all_right_truncatable_prime(nums):
    x = nums[8]
    def is_prime(n):
        if n < 2: 
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i: 
                return False
        return True

    def is_right_truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[:len(s)-i])):
                return False
        return True

    truncated_primes = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    truncated_primes.sort(reverse=True)
    return truncated_primes
