def find_n_th_smallest_num(nums):
    if len(nums) < 97:
        raise ValueError("The index 56 to index 96 is out of bounds")
    return sorted(nums)[len(nums) - 97]
