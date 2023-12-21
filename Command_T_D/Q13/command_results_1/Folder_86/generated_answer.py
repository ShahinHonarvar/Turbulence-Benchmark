
def find_second_largest_num(nums):
    second_largest = nums[-2]
    if second_largest == nums[-1]:
        return None
    return second_largest
