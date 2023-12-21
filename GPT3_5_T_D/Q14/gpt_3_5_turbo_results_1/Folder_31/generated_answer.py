
def find_second_smallest_num(numbers):
    nums = numbers[29:94]
    if len(set(nums)) <= 1:  # check if there is only one or zero elements
        return None
    else:
        nums.sort()
        return nums[1]
