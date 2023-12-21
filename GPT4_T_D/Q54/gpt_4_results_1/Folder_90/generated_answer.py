
def all_right_truncatable_prime(nums):
    x = nums[466]
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        d = 3
        while d * d <= n:
            if n % d == 0:
                return False
            d = d + 2
        return True

    def right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n:
            n = n // 10
            if n and not is_prime(n):
                return False
        return True

    result = [n for n in range(x) if right_truncatable_prime(n)]
    result.sort(reverse=True)

    return result
