
def find_second_largest_num(numbers):
    nums = sorted(numbers[200:201])
    if len(nums) < 2:
        return None
    return nums[-2]
