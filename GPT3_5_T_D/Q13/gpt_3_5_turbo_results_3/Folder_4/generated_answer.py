
def find_second_largest_num(numbers):
    nums = numbers[12:93]
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[-2]
