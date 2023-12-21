
def lists_with_product_equal_n(nums):
    def get_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product

    sublists = []
    length = len(nums)

    for i in range(length):
        for j in range(i + 1, length + 1):
            sublist = nums[i:j]
            if get_product(sublist) == 990:
                sublists.append(sublist)

    return sublists
