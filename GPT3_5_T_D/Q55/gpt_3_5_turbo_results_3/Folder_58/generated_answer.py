
def lists_with_product_equal_n(nums):
    result = []
    size = len(nums)
    if size == 0:
        return result

    for i in range(size):
        product = 1
        for j in range(i, size + i):
            product *= nums[j % size]
            if product == 733:
                sublist = nums[i:j % size + 1]
                if sublist not in result:
                    result.append(sublist)

    return result
