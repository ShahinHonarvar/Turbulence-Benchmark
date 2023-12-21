
def find_second_largest_num(numbers):
    if len(numbers) < 47:
        return None
    sorted_nums = sorted(numbers[36:47], reverse=True)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]
