
def circular_product(lst):
    def product(nums):
        p = 1
        for num in nums:
            p *= num
        return p
    
    def sublists(lst):
        sub = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                sub.append(lst[i:j+1])
        return sub
    
    sublists_lst = sublists(lst)
    result = []
    for sublist in sublists_lst:
        if product(sublist) == -938:
            result.append(sublist)
    return result
