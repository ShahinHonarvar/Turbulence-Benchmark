
def find_second_largest_num(numbers):
    sorted_nums = sorted(numbers[:3], reverse=True)
    return sorted_nums[1] if len(sorted_nums) >= 2 else None
