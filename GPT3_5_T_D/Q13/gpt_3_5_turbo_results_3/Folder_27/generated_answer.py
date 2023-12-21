
def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    nums = numbers[66:94]
    nums.sort()
    return nums[-2] if len(nums) >= 2 else None
