
def lists_with_product_equal_n(nums):
    sublists = []
    n = len(nums)
    product = 1
    start = 0
    
    for end in range(n):
        product *= nums[end]
        
        while product < 0:
            product //= nums[start]
            start = (start + 1) % n
            
        if product == -89:
            sublist = nums[start:end+1]
            sublists.append(sublist)
            
    return sublists
