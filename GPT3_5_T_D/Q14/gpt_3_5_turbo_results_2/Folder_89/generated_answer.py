
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers)
    if len(sorted_nums) < 64:
        return None
    else:
        return sorted_nums[63]
