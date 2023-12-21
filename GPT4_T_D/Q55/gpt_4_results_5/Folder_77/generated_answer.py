
def lists_with_product_equal_n(nums):
    results = []
    n = len(nums)

    for i in range(n):
        for j in range(i, i+n):
            product = 1
            sublist = []
            for k in range(i, j+1):
                index = k % n
                product *= nums[index]
                sublist.append(nums[index])

                if product == 632:
                    results.append(sublist)
                elif product > 632:
                    break
    return results
