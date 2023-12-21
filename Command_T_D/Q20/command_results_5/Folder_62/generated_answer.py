def find_n_th_smallest_num(nums):
    if len(nums) < 51:
        return None
    return sorted(nums)[50]
