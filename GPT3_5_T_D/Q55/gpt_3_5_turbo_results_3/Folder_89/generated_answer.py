
from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    def get_sublists_with_product(nums: List[int], target: int) -> List[List[int]]:
        sublists = []
        n = len(nums)
        product_so_far = 1
        start, end = 0, 0
        
        while end < n:
            product_so_far *= nums[end]
            
            while start <= end and product_so_far > target:
                product_so_far //= nums[start]
                start += 1
            
            if product_so_far == target:
                sublists.append(nums[start:end+1])
            
            end += 1
        
        return sublists
    
    n = len(nums)
    if n == 0:
        return []
    
    sublists = []
    
    for i in range(n):
        sublists += get_sublists_with_product(nums[i:] + nums[:i], 57)
    
    return sublists
