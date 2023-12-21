
def composite_nums_between_indices(nums):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    composite_nums = set()
    for i in range(29, 94):
        if is_prime(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums
