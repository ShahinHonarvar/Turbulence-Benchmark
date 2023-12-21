
def find_second_largest_num(numbers):
    nums = numbers[20:31]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]
