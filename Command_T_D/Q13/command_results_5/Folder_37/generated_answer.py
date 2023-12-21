
def find_second_largest_num(nums):
    second_largest = max(nums[:5], key=lambda x: x)
    return second_largest
