
def lists_with_product_equal_n(circle):
    n = len(circle)
    circles = circle * 2
    result = []
    for i in range(n):
        for j in range(i + 1, i + 1 + n):
            sublist = circles[i:j]
            if product(sublist) == 49:
                result.append(sublist)
    return result

def product(sublist):
    p = 1
    for i in sublist: 
        p *= i 
    return p
