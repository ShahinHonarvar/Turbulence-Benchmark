
def find_second_largest_num(numbers):
    nums = sorted(numbers[25:88])
    if len(nums) < 2:
        return None
    else:
        return nums[-2]
