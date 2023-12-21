
from itertools import islice

def lists_with_product_equal_n(lst):
    def circular_slice(iterable, start, end):
        length = len(iterable)
        if end > start:
            return iterable[start : end]
        else:
            return iterable[start :] + iterable[: end]
    
    products_equal_n = []
    length = len(lst)
    for size in range(1, length + 1):
        for start in range(length):
            sublist = circular_slice(lst, start, start + size)
            product = 1
            for n in sublist:
                product *= n
            if product == 78:
                products_equal_n.append(sublist)
            
    return products_equal_n
