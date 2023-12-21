
def composite_nums_between_indices(list_of_nums):
    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    composite_nums = set()
    for index in range(50, 55):
        if index < len(list_of_nums) and is_composite(list_of_nums[index]):
            composite_nums.add(list_of_nums[index])
    return composite_nums
