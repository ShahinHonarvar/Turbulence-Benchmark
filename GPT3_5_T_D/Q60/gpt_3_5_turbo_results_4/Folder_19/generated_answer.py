
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if not is_prime(n):
            return False
        while n > 9:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True

    def is_right_truncatable(n):
        if not is_prime(n):
            return False
        while n > 9:
            n = int(str(n)[:-1])
            if not is_prime(n):
                return False
        return True

    x = nums[67]
    result = []
    for i in range(2, x+1):
        if '0' in str(i):
            continue
        if is_left_truncatable(i) and is_right_truncatable(i):
            result.append(i)

    return sorted(result, reverse=True)
