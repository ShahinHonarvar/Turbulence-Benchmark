
def find_second_smallest_num(numbers):
    if len(numbers) < 976:
        return None
    sorted_nums = sorted(numbers[639:976])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]
