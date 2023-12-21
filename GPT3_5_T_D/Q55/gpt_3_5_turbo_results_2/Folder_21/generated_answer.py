
from itertools import accumulate
from operator import mul

def lists_with_product_equal_n(lst):
    def get_product(sublist):
        if len(sublist) > 0:
            return accumulate(sublist, mul)
    
    sublists = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            product = get_product(lst[i:j])
            if product and product[-1] == 851:
                sublists.append(lst[i:j])
    
    return sublists
