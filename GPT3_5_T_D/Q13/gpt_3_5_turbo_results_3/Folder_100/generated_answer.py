
def find_second_largest_num(numbers):
    sorted_nums = sorted(set(numbers[42:69]), reverse=True)
    return sorted_nums[1] if len(sorted_nums) > 1 else None
