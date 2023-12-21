
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers[66:78])
    if len(sorted_nums) < 2:
        return None
    else:
        return sorted_nums[1]
