
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers[91:100])
    if len(sorted_nums) > 1:
        return sorted_nums[1]
    else:
        return None
