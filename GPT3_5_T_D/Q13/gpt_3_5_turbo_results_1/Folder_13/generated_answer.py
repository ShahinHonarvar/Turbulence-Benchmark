
def find_second_largest_num(numbers):
    if len(numbers) < 88:
        return None
    nums = numbers[25:88]
    nums.sort()
    return nums[-2] if len(nums) > 1 else None
