
def find_second_largest_num(numbers):
    if len(numbers) < 88:
        return None
    sorted_nums = sorted(numbers[25:88], reverse=True)
    if len(sorted_nums) > 1:
        return sorted_nums[1]
    else:
        return None
