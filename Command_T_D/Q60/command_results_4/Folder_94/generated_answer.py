
def all_left_right_truncatable_prime(nums):
    def is_left_right_truncatable(n):
        if n <= 9:
            return True
        if str(n).count("0") != 0:
            return False
        for i in range(2, int(str(n)[0]) + 1):
            if n % i == 0:
                return False
        for i in range(2, int(str(n)[-1]) + 1):
            if n % i == 0:
                return False
        return True
    return sorted(filter(is_left_right_truncatable, nums))
