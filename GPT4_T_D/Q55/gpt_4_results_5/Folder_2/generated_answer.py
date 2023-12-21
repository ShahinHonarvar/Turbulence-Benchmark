
from collections import deque

def lists_with_product_equal_n(circle):
    circlist, result = deque(circle), []
    if len(circle) == 0:
        return []
    for _ in range(len(circle)):
        circlist.rotate(1)
        for i in range(len(circlist)):
            for j in range(i+1, len(circlist)+1):
                sublist = list(circlist)[i:j]
                product = 1
                for elem in sublist:
                    product *= elem
                if product == -968:
                    result.append(sublist)
    return result
