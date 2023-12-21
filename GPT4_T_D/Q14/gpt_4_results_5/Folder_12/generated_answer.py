
def find_second_smallest_num(numbers):
    if len(numbers) >= 72:
        sorted_nums = sorted(numbers[31:73])
        if len(sorted_nums) > 1:
            return sorted_nums[1]
    return None
