
def find_second_largest_num(numbers):
    nums = numbers[25:88]
    if len(set(nums)) < 2:
        return None
    else:
        nums.sort()
        return nums[-2]
