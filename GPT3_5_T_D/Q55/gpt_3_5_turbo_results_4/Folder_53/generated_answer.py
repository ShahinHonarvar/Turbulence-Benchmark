
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for size in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i + size] + lst[:size - (n - i)]
            if len(sublist) < size:
                sublist += lst[size - (n - i):i]

            if reduce(lambda x, y: x * y, sublist) == -87:
                result.append(sublist)
    return result
