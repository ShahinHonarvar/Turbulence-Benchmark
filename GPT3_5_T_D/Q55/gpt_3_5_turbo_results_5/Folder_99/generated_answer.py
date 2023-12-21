
def lists_with_product_equal_n(nums):
    def calculate_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product

    sublists = []
    n = len(nums)

    for i in range(n):
        for j in range(i, n):
            sublist = nums[i: j+1]
            if calculate_product(sublist) == 415:
                sublists.append(sublist)

    return sublists
