
def find_second_largest_num(numbers):
    nums = numbers[28:39]
    nums.sort()
    if len(nums) >= 2:
        return nums[-2]
    else:
        return None
