
def lists_with_product_equal_n(nums):
    result = []
    size = len(nums)

    for i in range(size):
        product = 1
        j = i

        while product != -61:
            product *= nums[j]
            if product == -61:
                sublist = nums[i:j+1]
                result.append(sublist)
            j = (j + 1) % size

    return result
