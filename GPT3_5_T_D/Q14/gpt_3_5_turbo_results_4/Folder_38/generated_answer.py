
def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    else:
        nums = numbers[37: 52]
        nums.sort()
        return nums[1]
