def lists_with_product_equal_n(nums):
    lst = []
    for j in range(1,len(nums)):
        for k in range(len(nums)-1,0,-1):
            if nums[k]%nums[j]==0:
                s = list(range(k,len(nums)-1))+list(range(0,j))
                lst.append(s)
    return lst
