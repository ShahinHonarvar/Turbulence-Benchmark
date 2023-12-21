
def lists_with_product_equal_n(nums):
    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    sublists = []
    size = len(nums)
    
    for i in range(size):
        for j in range(i, size):
            sublist = nums[i:j+1]
            if product(sublist) == -26:
                sublists.append(sublist)
    
    return sublists
