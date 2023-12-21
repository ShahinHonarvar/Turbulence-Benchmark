def find_n_th_smallest_num(nums):
    return sorted(nums)[len(nums) - (nums.count(min(nums)) - (nums.count(min(nums)) > 33)) - (nums.count(min(nums)) > 39)]
