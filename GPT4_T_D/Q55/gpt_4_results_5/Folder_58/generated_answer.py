
from collections import deque

def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums  # duplicate the list to simulate the circular list
    result = []
    for i in range(n):
        for j in range(i+1, i+n+1):
            sublist = nums[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 733:
                result.append(sublist)
    return result
