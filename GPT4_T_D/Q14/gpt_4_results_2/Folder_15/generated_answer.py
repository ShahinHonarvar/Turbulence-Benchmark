
def find_second_smallest_num(numbers):
    if len(numbers) <= 1:
        return None
    else:
        sorted_nums = sorted(numbers[0:4])
        return sorted_nums[1] if len(sorted_nums) > 1 else None
