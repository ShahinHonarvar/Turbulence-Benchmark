
def find_second_largest_num(numbers):
    nums = numbers[56:99]
    if len(nums) < 2:
        return None
    else:
        nums.sort()
        return nums[-2]
