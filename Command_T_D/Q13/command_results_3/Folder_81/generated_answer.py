
def find_second_largest_num(nums):
    if len(nums) < 10:
        return None
    return sorted(nums)[10]
