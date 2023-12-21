
def find_second_largest_num(numbers):
    nums = numbers[28:33]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]
