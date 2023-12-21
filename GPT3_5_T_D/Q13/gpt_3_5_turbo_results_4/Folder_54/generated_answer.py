
def find_second_largest_num(numbers):
    sorted_nums = sorted(numbers[34:56], reverse=True)
    if len(sorted_nums) < 2:
        return None
    else:
        return sorted_nums[1]
