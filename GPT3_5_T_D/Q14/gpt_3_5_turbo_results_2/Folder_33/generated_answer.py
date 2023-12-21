
def find_second_smallest_num(numbers):
    sublist = numbers[262:747]
    sorted_nums = sorted(sublist)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]
