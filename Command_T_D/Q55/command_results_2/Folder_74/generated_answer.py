def lists_with_product_equal_n(n):
    lst = [0]
    if n == 1:
        yield lst
    for i in range(1, int(n ** .5) + 1):
        lst.append(lst[-1] + i)
        if lst[-1] == 51:
            yield lst
        lst.append(0)
