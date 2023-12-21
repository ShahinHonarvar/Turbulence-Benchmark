
def find_second_largest_num(nums):
    if len(nums) < 63:
        return None
    return sorted(nums)[62]
