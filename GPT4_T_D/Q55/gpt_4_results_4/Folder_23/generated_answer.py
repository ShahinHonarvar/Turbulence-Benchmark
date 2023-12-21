
def lists_with_product_equal_n(list):
    sublists = []
    n = len(list)
    for i in range(n):
        for j in range(i, n):
            prod = 1
            for element in list[i:j+1]:
                prod *= element
            if prod == -95:
                sublists.append(list[i:j+1])
        for j in range(0, i):
            prod = 1
            for element in list[j:i+n+1]:
                prod *= element
            if prod == -95:
                sublists.append(list[j:i+n+1])
    return sublists
