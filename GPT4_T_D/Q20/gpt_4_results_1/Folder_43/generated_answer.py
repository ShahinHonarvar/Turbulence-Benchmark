
def find_n_th_smallest_num(nums):
    sorted_nums = sorted(nums[28:65])
    try:
        return sorted_nums[15]
    except IndexError:
        return 'Index out of range'
