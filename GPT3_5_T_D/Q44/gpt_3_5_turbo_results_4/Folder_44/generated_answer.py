
def composite_nums_between_indices(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    composite_set = set()
    for i in range(64, 67):
        if not is_prime(nums[i]):
            composite_set.add(nums[i])
    return composite_set
