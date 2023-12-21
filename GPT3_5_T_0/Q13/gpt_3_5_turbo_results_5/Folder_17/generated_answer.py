
def find_second_largest_num(numbers):
    if len(numbers) < 79:
        return None
    sorted_nums = sorted(numbers[62:79], reverse=True)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]
