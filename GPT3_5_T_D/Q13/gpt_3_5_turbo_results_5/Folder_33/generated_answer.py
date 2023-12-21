
def find_second_largest_num(numbers):
    nums = numbers[667:775]
    if len(nums) < 2:
        return None
    largest = max(nums)
    nums.remove(largest)
    return max(nums) if len(nums) > 0 else None
