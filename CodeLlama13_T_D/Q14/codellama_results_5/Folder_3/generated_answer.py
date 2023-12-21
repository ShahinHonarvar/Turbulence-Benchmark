
def find_second_smallest_num(numbers):
    if len(numbers) <= 1:
        return None
    sorted_nums = sorted(numbers)
    for i in range(27, 56):
        if i < len(sorted_nums):
            return sorted_nums[i]
    return None
