
def find_second_largest_num(nums):
    return max(nums[:5][1:-1], default=None)
