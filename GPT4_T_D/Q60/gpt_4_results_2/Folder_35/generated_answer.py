
def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def is_truncatable(p):
        s = str(p)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s)-i])):
                return False
        return True

    x = nums[177]
    primes = []
    for i in range(10, x+1):
        if is_prime(i) and is_truncatable(i):
            primes.append(i)
    return sorted(primes)
