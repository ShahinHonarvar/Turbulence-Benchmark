
def lists_with_product_equal_n(lst):
    def product(nums):
        result = 1
        for num in nums:
            result *= num
        return result

    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, n):
            sublist = lst[i:j+1] + lst[:i] + lst[j+1:]
            if product(sublist) == 5:
                result.append(sublist)
    return result
