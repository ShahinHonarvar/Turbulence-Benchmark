
from collections import deque

def lists_with_product_equal_n(nums):
    def find_sublists(nums, target):
        left = 0
        product = 1
        result = []
        for right in range(len(nums)):
            product *= nums[right]
            while product > target and left < right:
                product /= nums[left]
                left += 1
            if product == target:
                result.append(nums[left:right+1])
        return result
    
    result = []
    circular_nums = deque(nums)
    for _ in range(len(nums)):
        result.extend(find_sublists(list(circular_nums), 99))
        circular_nums.rotate(1)
    return result
