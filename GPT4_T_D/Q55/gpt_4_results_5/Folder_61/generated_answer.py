
def lists_with_product_equal_n(nums):
    results = []
    size = len(nums)

    for i in range(size):
        for j in range(1, size+1):
            if i + j <= size:
                sublist = nums[i:i+j]
                product = 1
                for num in sublist:
                    product *= num
                if product == -10:
                    results.append(sublist)
            else:
                sublist = nums[i:] + nums[:j-size]
                product = 1
                for num in sublist:
                    product *= num
                if product == -10:
                    results.append(sublist)

    return results
