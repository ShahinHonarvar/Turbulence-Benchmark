
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
        if not is_prime(n):
            return False

        digits = str(n)
        for i in range(1, len(digits)):
            left = int(digits[i:])
            right = int(digits[:-i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True

    x = nums[77]
    result = []
    for num in range(x, 0, -1):
        if is_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result
