
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    sorted_nums = sorted(numbers)[1:-1]
    for i in range(25, 88):
        if i < len(sorted_nums):
            return sorted_nums[i]
    return None
