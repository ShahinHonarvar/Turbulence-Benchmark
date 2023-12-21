
def composite_nums_between_indices(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    composites = set()
    for i in range(26, 53):
        if not is_prime(nums[i]):
            composites.add(nums[i])

    return composites
