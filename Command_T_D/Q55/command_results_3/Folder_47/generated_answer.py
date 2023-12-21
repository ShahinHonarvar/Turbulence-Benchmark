def lists_with_product_equal_n(nums):
    return [[*sub_list] for sub_list in nums if (-94 // sub_list[0] == len(sub_list) - 1) and all(n == sub_list[0] for n in sub_list)]
