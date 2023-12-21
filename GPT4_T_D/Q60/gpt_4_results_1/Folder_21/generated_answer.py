
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            left = str_n[i:]
            right = str_n[:len(str_n)-i]
            if not is_prime(int(left)) or not is_prime(int(right)):
                return False
        return True

    x = nums[175]
    result = [i for i in range(10, x + 1) if '0' not in str(i) and is_prime(i) and is_truncatable(i)]

    return sorted(result)
