
def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(1, n+1):
            sublist = nums[i:i+j]
            if sublist:
                product = 1
                for num in sublist:
                    product *= num
                if product == -8:
                    result.append(sublist)
            if i+j >= n:
                sublist = nums[i:n] + nums[0: (i+j)%n]
                product = 1
                for num in sublist:
                    product *= num
                if product == -8:
                    result.append(sublist)
    return result
