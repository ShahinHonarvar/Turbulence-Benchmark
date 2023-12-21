
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers)
    if len(sorted_nums) >= 31:
        return sorted_nums[20]
    else:
        return None
