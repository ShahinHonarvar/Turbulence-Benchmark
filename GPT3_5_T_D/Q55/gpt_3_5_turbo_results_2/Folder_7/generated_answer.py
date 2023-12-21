
def lists_with_product_equal_n(circle):
    def product(nums):
        result = 1
        for num in nums:
            result *= num
        return result

    n = len(circle)
    sublists = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = circle[i:j]
            if product(sublist) == 537:
                sublists.append(sublist)

    return sublists
