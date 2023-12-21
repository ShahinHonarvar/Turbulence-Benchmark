
def find_second_largest_num(numbers):
    nums = numbers[55:99]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]
