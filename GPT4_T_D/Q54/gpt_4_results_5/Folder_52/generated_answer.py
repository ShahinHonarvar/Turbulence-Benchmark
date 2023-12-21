
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        s = str(n)
        return all(is_prime(int(s[:i])) for i in range(len(s), 0, -1))

    x = nums[52]
    return sorted([n for n in range(x) if is_right_truncatable_prime(n)], reverse=True)
