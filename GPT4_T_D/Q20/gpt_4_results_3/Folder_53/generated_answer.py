
def find_n_th_smallest_num(nums):
    sorted_nums = sorted(nums[19:191])
    try:
        return sorted_nums[18]
    except IndexError:
        return "List doesn't have 19 elements in the range 19 to 190"
