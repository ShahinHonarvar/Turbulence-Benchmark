
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:len(str(n))-i])):
                return False
        return True

    x = nums[77]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)
