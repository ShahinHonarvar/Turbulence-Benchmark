
def find_second_smallest_num(numbers):
    if len(numbers) < 36:
        return None
    else:
        sorted_nums = sorted(numbers[32:36])
        if len(sorted_nums) < 2:
            return None
        return sorted_nums[1]
