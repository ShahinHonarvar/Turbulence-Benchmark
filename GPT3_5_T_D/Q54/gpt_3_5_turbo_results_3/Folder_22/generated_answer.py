
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def truncate(num):
        num_str = str(num)
        for i in range(len(num_str), 0, -1):
            if not is_prime(int(num_str[:i])):
                return False
        return True

    x = nums[85]
    result = []
    for i in range(2, x):
        if is_prime(i) and truncate(i):
            result.append(i)

    return sorted(result)
