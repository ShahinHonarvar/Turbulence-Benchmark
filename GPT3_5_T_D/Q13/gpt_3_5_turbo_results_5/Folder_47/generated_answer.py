
def find_second_largest_num(numbers):
    if len(numbers) < 77:
        return None
    nums = sorted(numbers[37:77])
    if len(nums) < 2:
        return None
    return nums[-2]
