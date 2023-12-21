def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        prod = 1
        curr_list = []
        for j in range(i, len(nums)):
            prod *= nums[j]
            curr_list.append(nums[j])
            if prod == 733:
                result += [[*curr_list]]
                curr_list = []
                prod = 1
    return result
