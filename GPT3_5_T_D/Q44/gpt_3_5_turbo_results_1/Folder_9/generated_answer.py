
def composite_nums_between_indices(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    start_index = 80
    end_index = 200
    composite_nums = set()
    for i in range(start_index, end_index + 1):
        if not is_prime(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums
