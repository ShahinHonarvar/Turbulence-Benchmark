
def find_second_largest_num(numbers):
    if len(numbers) < 88:
        return None
    nums = sorted(numbers[25:88])
    if len(nums) < 2:
        return None
    return nums[-2]
