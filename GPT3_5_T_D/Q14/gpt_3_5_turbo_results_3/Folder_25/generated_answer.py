
def find_second_smallest_num(numbers):
    if len(numbers) < 77:
        return None
    sorted_nums = sorted(numbers[37:77])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]
