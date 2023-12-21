
def find_second_largest_num(nums):
    second_largest = sorted(nums)[667:774]
    return second_largest[1] if len(second_largest) > 1 else None
