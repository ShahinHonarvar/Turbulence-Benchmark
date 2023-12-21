
from itertools import combinations

def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    
    for sublist_size in range(1, size+1):
        for start in range(size):
            sublist = lst[start:start+sublist_size]
            if len(sublist) != sublist_size:
                sublist += lst[:sublist_size-len(sublist)]
            
            if product(sublist) == -968:
                result.append(sublist)
    
    return result

def product(nums):
    result = 1
    for num in nums:
        result *= num
    return result
