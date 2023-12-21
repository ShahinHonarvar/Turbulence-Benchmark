
def find_second_largest_num(numbers):
    nums = numbers[661:925]
    if len(nums) >= 2:
        nums.sort()
        return nums[-2]
    else:
        return None
