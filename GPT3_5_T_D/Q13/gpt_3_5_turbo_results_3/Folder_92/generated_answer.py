
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    sorted_nums = sorted(numbers, reverse=True)
    return sorted_nums[1]
