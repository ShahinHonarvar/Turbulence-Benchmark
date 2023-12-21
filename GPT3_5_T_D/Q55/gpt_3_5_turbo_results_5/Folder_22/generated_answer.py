
from itertools import combinations

def lists_with_product_equal_n(nums):
    result = []
    size = len(nums)
    for i in range(1, size + 1):
        for j in range(size):
            sublist = nums[j:j+i]
            if len(sublist) == i and not 0 in sublist:
                product = 1
                for num in sublist:
                    product *= num
                if product == 4:
                    result.append(sublist)
    return result
