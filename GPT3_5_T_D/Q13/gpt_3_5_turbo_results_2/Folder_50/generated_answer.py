
def find_second_largest_num(numbers):
    if len(numbers) < 85:
        return None
    nums = numbers[70:85]
    nums.sort()
    return nums[-2] if len(nums) >= 2 else None
