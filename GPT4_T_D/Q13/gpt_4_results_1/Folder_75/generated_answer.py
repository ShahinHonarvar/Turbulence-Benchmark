
def find_second_largest_num(numbers):
    if len(numbers) < 58:
        return None
    else:
        sorted_nums = sorted(numbers[56:58])
        if len(sorted_nums) == 2:
            return sorted_nums[0]
        else:
            return None
