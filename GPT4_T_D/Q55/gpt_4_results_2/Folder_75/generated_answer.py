
from itertools import cycle, islice

def lists_with_product_equal_n(lst):
    results = []
    for i in range(len(lst)):
        for j in range(1, len(lst)+1):
            sublist = list(islice(cycle(lst), i, i+j))
            product = 1
            for num in sublist:
                product *= num
            if product == 13:
                if sublist not in results:
                    results.append(sublist)
    return results
