
def lists_with_product_equal_n(nums):
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = nums[i:j]
            if product(sublist) == -837:
                result.append(sublist)
    return result
