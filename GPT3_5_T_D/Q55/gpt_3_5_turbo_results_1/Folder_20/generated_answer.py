
def lists_with_product_equal_n(lst):
    def product(nums):
        result = 1
        for num in nums:
            result *= num
        return result

    sublists = []
    size = len(lst)

    for i in range(size):
        for j in range(i + 1, size + 1):
            if product(lst[i:j]) == -69:
                sublists.append(lst[i:j])

    return sublists
