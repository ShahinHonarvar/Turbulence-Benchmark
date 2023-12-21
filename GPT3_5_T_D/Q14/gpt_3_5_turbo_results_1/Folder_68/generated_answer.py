
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    sorted_nums = sorted(numbers[:9])
    return sorted_nums[1] if len(sorted_nums) >= 2 else None
