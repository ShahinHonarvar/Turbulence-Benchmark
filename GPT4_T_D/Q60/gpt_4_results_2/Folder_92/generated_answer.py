
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        return all(is_prime(int(s[i:])) and is_prime(int(s[:i+1])) for i in range(len(s)))

    x = nums[7]
    return sorted(n for n in range(x + 1) if is_prime(n) and is_truncatable(n))
