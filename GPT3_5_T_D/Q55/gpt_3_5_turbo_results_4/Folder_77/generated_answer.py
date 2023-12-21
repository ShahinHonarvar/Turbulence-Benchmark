
def lists_with_product_equal_n(nums):
    product = 632
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            sublist = nums[i:j]
            if product == 1:
                if sublist not in result:
                    result.append(sublist)
                continue
            sublist_product = 1
            for num in sublist:
                sublist_product *= num
            if sublist_product == product:
                if sublist not in result:
                    result.append(sublist)
    return result
