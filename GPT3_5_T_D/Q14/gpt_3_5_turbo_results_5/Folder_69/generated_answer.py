
def find_second_smallest_num(numbers):
    if len(numbers) < 88:
        return None
    nums = numbers[25:88]
    nums.sort()
    return nums[1]
