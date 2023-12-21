
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers[62:93])
    if len(sorted_nums) >= 2:
        return sorted_nums[1]
    else:
        return None
