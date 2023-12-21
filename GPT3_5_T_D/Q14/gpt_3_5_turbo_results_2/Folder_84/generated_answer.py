
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers[40:81])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]
