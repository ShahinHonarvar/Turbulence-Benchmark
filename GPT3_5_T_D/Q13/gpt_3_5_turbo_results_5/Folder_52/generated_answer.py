
def find_second_largest_num(numbers):
    if len(numbers) < 39:
        return None
    sorted_nums = sorted(numbers[28:39], reverse=True)
    return sorted_nums[1] if len(sorted_nums) >= 2 else None
