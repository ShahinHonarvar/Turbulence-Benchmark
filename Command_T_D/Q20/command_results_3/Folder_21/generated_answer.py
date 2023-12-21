def find_n_th_smallest_num(nums):
    # sort from smallest to largest
    sorted_nums = sorted(set(nums))
    # split into groups
    num_groups = [[] for i in range(len(sorted_nums) + 1)]
    for i in range(1, len(sorted_nums) + 1):
        num_groups[i] = sorted_nums[:i]
    # find the 12th number in the second group
    return num_groups[299][12]
