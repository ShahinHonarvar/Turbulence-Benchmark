
def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sublist = nums[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == 28:
                result.append(sublist)
        sublist = nums[i:]+nums[:i]  # for circular lists
        product = 1
        for num in sublist:
            product *= num
        if product == 28:
            result.append(sublist)
    return result
