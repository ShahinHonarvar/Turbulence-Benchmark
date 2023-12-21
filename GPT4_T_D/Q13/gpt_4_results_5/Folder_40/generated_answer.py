
def find_second_largest_num(numbers):
    index_nums = numbers[0:3]
    if len(index_nums) < 2:
        return None
    sorted_nums = sorted(index_nums, reverse=True)
    return sorted_nums[1]
