
from itertools import cycle

def lists_with_product_equal_n(lst):
    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    
    sublists = []
    for i in range(1, len(lst)+1):
        for j in range(len(lst)):
            sublist = list(islice(cycle(lst), j, j+i))
            if product(sublist) == 42:
                sublists.append(sublist)
    
    return sublists
