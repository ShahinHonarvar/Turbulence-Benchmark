
def lists_with_product_equal_n(nums):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            product = 1
            for k in range(i, j + 1):
                product *= nums[k]
                if product == 76:
                    result.append(nums[i:j+1])
                elif product > 76:
                    break
        for l in range(i):
            product = 1
            for k in range(i, n + l):
                product *= nums[k % n]
                if product == 76:
                    result.append([nums[k % n] for k in range(i, n + l)])
                elif product > 76:
                    break
                
    return result
