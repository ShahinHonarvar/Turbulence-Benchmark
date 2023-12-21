
def find_second_largest_num(numbers):
    if len(numbers) <= 94:
        return None
    sorted_nums = sorted(numbers)[75:95]
    second_largest = sorted_nums[1]
    return second_largest
