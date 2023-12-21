
from collections import deque

def lists_with_product_equal_n(circ_list):
    n = len(circ_list)
    circ_list = deque(circ_list)
    result = []

    for _ in range(n):
        for i in range(1, n + 1):
            for j in range(n):
                sublist = [circ_list[(j + k) % n] for k in range(i)]
                product = 1
                for number in sublist:
                    product *= number
                if product == -94:
                    result.append(sublist)
        circ_list.rotate(1)

    return result
