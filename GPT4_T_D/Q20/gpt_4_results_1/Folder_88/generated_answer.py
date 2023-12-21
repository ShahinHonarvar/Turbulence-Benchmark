
def find_n_th_smallest_num(nums):
    try:
        return sorted(nums[1:9])[7]
    except IndexError:
        return "The list should have at least 9 elements"
