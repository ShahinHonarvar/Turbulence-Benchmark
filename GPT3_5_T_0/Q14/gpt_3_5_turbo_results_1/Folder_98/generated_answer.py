
def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    sorted_nums = sorted(numbers[6:7])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]
