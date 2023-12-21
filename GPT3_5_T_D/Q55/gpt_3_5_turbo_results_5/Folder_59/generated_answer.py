
def lists_with_product_equal_n(nums):
    def product_equal_n(start):
        sublist = []
        product = 1
        i = start
        while True:
            sublist.append(nums[i])
            product *= nums[i]
            if product == -3:
                return sublist
            i = (i + 1) % len(nums)
            if i == start:
                return None

    result = []
    for i in range(len(nums)):
        sublist = product_equal_n(i)
        if sublist is not None:
            result.append(sublist)

    return result
