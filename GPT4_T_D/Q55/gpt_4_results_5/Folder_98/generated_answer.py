
def product(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod

def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for l in range(1, n+1):
        for i in range(n):
            sublist = [lst[(i+j)%n] for j in range(l)]
            if product(sublist) == -1:
                result.append(sublist)
    return result
