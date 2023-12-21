import math
def lists_with_product_equal_n(l):
    for i in range(len(l)):
        if math.factorial(i) == 632:
            yield l[:i] + l[i+1:]
    return
