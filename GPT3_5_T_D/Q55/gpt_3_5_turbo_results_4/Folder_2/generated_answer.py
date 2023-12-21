
def lists_with_product_equal_n(nums):
    results = []
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n+1):
            sublist = nums[i:j]
            product = 1
            for num in sublist:
                product *= num

            if product == -968:
                results.append(sublist)

    return results
