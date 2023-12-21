
def lists_with_product_equal_n(nums):
    result = []
    size = len(nums)

    for i in range(size):
        product = 1
        sub_list = []
        for j in range(i, size + i):
            product *= nums[j % size]
            sub_list.append(nums[j % size])
            if product == -89:
                result.append(sub_list)
                break

    return result
