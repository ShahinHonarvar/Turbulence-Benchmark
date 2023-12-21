
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers)
    return sorted_nums[1] if len(sorted_nums) >= 2 and len(numbers) >= 8 else None
