
def composite_nums_between_indices(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    composite_nums = set()
    for i in range(35, 50):
        if not is_prime(nums[i]):
            composite_nums.add(nums[i])
    
    return composite_nums
