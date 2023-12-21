
def lists_with_product_equal_n(nums):
    sublists = []
    n = len(nums)
    for size in range(1, n+1):
        for start in range(n):
            sublist = [nums[(start+i)%n] for i in range(size)]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == 93:
                sublists.append(sublist)
    return sublists
