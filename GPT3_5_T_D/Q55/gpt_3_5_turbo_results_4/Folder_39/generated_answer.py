
def lists_with_product_equal_n(nums):
    n = len(nums)
    all_sublists = []
    product = 1
    start = 0
    end = 0
    
    while start < n:
        while end < n + start:
            product *= nums[end % n]
            
            if product == -46:
                all_sublists.append(nums[start:end % n + 1])
        
            end += 1
        
        product //= nums[start]
        start += 1
    
    return all_sublists
