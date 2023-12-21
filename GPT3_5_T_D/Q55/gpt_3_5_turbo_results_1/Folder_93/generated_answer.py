
def lists_with_product_equal_n(lst):
    def product(nums):
        p = 1
        for num in nums:
            p *= num
        return p

    sublists = []
    size = len(lst)
    for i in range(size):
        for j in range(i + 1, size + 1):
            sublist = lst[i:j]
            if product(sublist) == -91:
                sublists.append(sublist)
    return sublists
