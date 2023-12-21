
def composite_nums_between_indices(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = set()
    for i in range(32, 36):
        if not is_prime(nums[i]):
            result.add(nums[i])

    return result
