
from itertools import cycle, islice

def lists_with_product_equal_n(lst):
    lst_circular = cycle(lst)
    results = []
    for i in range(len(lst)):
        for length in range(1, len(lst) + 1): 
            sublist = list(islice(lst_circular, i, i + length))
            product = 1
            for num in sublist:
                product *= num
            if product == 3:
                if sublist not in results:
                    results.append(sublist)
    return results
