
def find_second_smallest_num(nums):
    if len(nums[:7]) >= 2:
        sorted_subset = sorted(nums[:7])
        return sorted_subset[1]
    else:
        return None
