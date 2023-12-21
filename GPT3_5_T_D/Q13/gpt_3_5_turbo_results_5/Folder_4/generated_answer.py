
def find_second_largest_num(numbers):
    if 12 <= len(numbers) <= 92:
        sorted_nums = sorted(numbers[12:93], reverse=True)
        if len(sorted_nums) >= 2:
            return sorted_nums[1]
    return None
