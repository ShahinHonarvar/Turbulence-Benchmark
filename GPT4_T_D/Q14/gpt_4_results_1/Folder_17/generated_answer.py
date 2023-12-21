
def find_second_smallest_num(numbers):
    if len(numbers[28:39]) < 2:
        return None
    sorted_nums = sorted(numbers[28:39])
    return sorted_nums[1]
