
def find_second_largest_num(numbers):
    if len(numbers) < 4:
        return None
    sorted_nums = sorted(numbers)[-4:]
    second_largest = sorted_nums[1]
    return second_largest
