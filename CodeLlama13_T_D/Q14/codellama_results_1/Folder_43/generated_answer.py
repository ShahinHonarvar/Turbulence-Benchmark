
def find_second_smallest_num(numbers):
    if len(numbers) < 95:
        return None
    sorted_nums = sorted(numbers)
    for i in range(74, 96):
        if i == 74 or sorted_nums[i] != sorted_nums[i-1]:
            return sorted_nums[i]
    return None
