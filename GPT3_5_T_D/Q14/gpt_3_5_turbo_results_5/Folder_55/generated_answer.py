
def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    else:
        sorted_nums = sorted(numbers[10:11])
        if len(sorted_nums) < 2:
            return None
        else:
            return sorted_nums[1]
