
def lists_with_product_equal_n(nums):
    results = []
    n = len(nums)

    for start in range(n):
        for end in range(start, start + n):
            sublist = nums[start:end%n+1] if end < n else nums[start:n] + nums[:end%n+1]
            product = 1
            for num in sublist:
                product *= num
            if product == -33:
                results.append(sublist)
    return results
