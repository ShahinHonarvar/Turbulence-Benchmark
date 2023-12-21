
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers[22:64])
    if len(sorted_nums) > 1:
        return sorted_nums[1]
    else:
        return None
