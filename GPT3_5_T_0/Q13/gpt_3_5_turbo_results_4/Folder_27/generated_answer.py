
def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    sorted_nums = sorted(numbers[66:94], reverse=True)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]
