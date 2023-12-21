
def all_right_truncatable_prime(nums):
    x = nums[71] if len(nums) > 71 else 0

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(n**0.5) + 1
        for div in range(3, max_div, 2):
            if n % div == 0:
                return False
        return True

    def is_right_truncatable(n):
        str_n = str(n)
        while len(str_n) > 1:
            str_n = str_n[:-1]
            if not is_prime(int(str_n)):
                return False
        return True

    primes = [i for i in range(2, x) if is_prime(i)]
    return sorted([p for p in primes if is_right_truncatable(p)], reverse=True)
