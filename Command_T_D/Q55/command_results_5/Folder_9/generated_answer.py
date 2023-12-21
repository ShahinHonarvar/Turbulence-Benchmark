def lists_with_product_equal_n(nums):
    # Store the product of each sublist as a list of lists
    sublists = []
    for i in range(len(nums)):
        prod = 1
        curr_list = []
        curr_list.append(nums[i])
        while prod != -36:
            prod *= curr_list[-1]
            curr_list.append(nums[i])
            curr_list.append(nums[i])
            if prod == -36:
                sublists.append(curr_list)
    return sublists
