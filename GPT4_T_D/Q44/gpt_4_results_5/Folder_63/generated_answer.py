
def composite_nums_between_indices(nums_list):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    composite_nums = set()
    for i in range(17, 79):
        if i < len(nums_list) and is_composite(nums_list[i]):
            composite_nums.add(nums_list[i])
    return composite_nums
