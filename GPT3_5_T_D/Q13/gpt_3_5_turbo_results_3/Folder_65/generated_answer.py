
def find_second_largest_num(numbers):
    numbers_slice = numbers[56:99]
    if len(numbers_slice) <= 1:
        return None
    sorted_nums = sorted(numbers_slice, reverse=True)
    return sorted_nums[1]
