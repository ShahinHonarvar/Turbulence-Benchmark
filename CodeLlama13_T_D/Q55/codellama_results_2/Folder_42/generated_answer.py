
def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        product = 1
        sublist = [nums[i]]
        for j in range(i+1, len(nums)):
            product *= nums[j]
            if product == n:
                result.append(sublist + [nums[j]])
                break
        else:
            continue
    return result
