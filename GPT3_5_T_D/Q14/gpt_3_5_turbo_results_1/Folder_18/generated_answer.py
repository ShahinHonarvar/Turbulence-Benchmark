
def find_second_smallest_num(numbers):
    sublist = numbers[30:49]
    if len(sublist) < 2:
        return None
    sorted_nums = sorted(sublist)
    return sorted_nums[1]
