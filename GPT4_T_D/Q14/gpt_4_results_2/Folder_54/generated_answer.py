
def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    else:
        sorted_nums = sorted(numbers[68:87])
        if len(sorted_nums) < 2:
            return None
        else:
            return sorted_nums[1]
