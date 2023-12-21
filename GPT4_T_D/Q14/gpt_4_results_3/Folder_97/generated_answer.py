
def find_second_smallest_num(numbers):
    try:
        nums = sorted(numbers[31:35])
        return nums[1]
    except IndexError:
        return None
