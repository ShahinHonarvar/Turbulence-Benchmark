
def lists_with_product_equal_n(nums):
    result = []
    length = len(nums)

    for i in range(length):
        sublist = []
        product = 1
        
        for j in range(i, length + i):
            index = j % length
            sublist.append(nums[index])
            product *= nums[index]

            if product == -32:
                result.append(sublist)
                break

    return result
