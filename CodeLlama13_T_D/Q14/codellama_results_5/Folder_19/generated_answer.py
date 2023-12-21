
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers)
    if len(sorted_nums) < 8:
        return None
    for i in range(4, 9):
        if sorted_nums[i] != sorted_nums[i-1]:
            return sorted_nums[i]
    return None
