
def find_second_largest_num(numbers):
    if len(numbers) < 62:
        return None
    sorted_nums = sorted(numbers[16:62], reverse=True)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]
