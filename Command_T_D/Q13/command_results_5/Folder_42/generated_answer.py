
def find_second_largest_num(nums):
    return sorted(set(nums))[29:80][1] if 29 <= len(set(nums)) <= 79 else None
