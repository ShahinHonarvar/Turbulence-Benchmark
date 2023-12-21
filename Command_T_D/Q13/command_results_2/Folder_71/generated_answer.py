
def find_second_largest_num(nums):
    return sorted(set(nums), key=lambda x: (x, x))[-2]
