
def all_left_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        n_str = str(n)
        while len(n_str) > 1:
            n_str = n_str[1:]
            if not is_prime(int(n_str)):
                return False
        return True

    x = nums[64]
    result = []
    for num in range(x - 1, 0, -1):
        if '0' not in str(num) and is_prime(num) and is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)
