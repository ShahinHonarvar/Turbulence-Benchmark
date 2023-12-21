
def find_second_smallest_num(numbers):
    numbers_slice = numbers[31:35]
    sorted_nums = sorted(numbers_slice)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]
