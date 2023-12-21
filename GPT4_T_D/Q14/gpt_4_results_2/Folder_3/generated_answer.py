
def find_second_smallest_num(numbers):
    if len(numbers) < 28:
        return None
    else:
        sorted_nums = sorted(numbers[27:56])
        return sorted_nums[1] if len(sorted_nums) > 1 else None
