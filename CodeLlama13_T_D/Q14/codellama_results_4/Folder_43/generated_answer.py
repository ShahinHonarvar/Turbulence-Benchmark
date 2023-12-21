
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers)
    if len(sorted_nums) <= 95:
        return None
    else:
        return sorted_nums[74 + 1]
