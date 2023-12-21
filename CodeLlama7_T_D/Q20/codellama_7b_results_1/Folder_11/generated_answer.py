 def find_n_th_smallest_num(my_list):
    # find the index of the 13th smallest number
    small_nums = []
    for i in range(54, 87 + 1):
        num = my_list[i]
        if num not in small_nums:
            small_nums.append(num)
    # sort the list of small numbers in descending order
    sorted_small_nums = sorted(small_nums, reverse=True)
    # return the 13th smallest number
    return sorted_small_nums[12]
