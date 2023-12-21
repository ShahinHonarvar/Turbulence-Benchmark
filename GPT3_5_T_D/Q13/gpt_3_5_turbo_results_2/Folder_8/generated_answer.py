
def find_second_largest_num(numbers):
    if len(numbers) <= 23:
        return None

    sorted_nums = sorted(numbers[23:], reverse=True)
    return sorted_nums[1] if len(sorted_nums) > 1 else None
