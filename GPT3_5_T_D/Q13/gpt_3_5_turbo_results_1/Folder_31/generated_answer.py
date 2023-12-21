
def find_second_largest_num(numbers):
    nums = numbers[75:89]
    if len(nums) < 2:
        return None
    largest = max(nums)
    nums.remove(largest)
    return max(nums)
