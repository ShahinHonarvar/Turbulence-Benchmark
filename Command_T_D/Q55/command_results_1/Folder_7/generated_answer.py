def lists_with_product_equal_n(nums):
    lst = []
    for j in range(len(nums)):
        prod = 1
        curr = nums[j]
        while curr:
            prod *= curr
            curr = nums[prod // curr - 1]
            if prod == 537:
                lst.append(nums[j:prod // curr])
                break
    return lst
