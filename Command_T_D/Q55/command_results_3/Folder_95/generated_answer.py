def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        curr_list = []
        curr_sum = 1
        curr_product = 1
        curr_value = nums[i]
        curr_list.append(curr_value)
        curr_sum += curr_value
        curr_product = curr_sum * curr_value
        curr_list = list(range(i, len(nums))) + curr_list
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            curr_product = curr_sum * nums[j]
            curr_list += list(range(j, len(nums)))
            if curr_product == 28:
                res += [curr_list]
    return res
