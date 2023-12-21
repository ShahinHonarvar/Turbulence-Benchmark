
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        digits = len(str(n))
        s = str(n)
        for i in range(digits - 1):
            s = s[:-1]
            if not is_prime(int(s)):
                return False
        s = str(n)
        for i in range(digits - 1):
            s = s[1:]
            if not is_prime(int(s)):
                return False
        return True

    x = nums[50]
    result = []
    for i in range(x, 0, -1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
