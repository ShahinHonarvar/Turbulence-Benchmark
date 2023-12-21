
def all_right_truncatable_prime(nums):
    x = nums[43]

    def is_prime(n):
        if n <= 1:
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

    def is_right_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True

    return sorted(filter(is_right_truncatable, filter(is_prime, range(x))))
