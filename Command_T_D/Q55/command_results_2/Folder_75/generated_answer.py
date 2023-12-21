def lists_with_product_equal_n(list1):
    if not list1:
        return []
    if len(list1) == 1:
        yield [list1]
        return
    for i in range(len(list1) - 1):
        x = list1[i]
        y = list1[i + 1]
        if x == y:
            continue
        if x == 13 or y == 13:
            yield [list1[:i + 1]]
            yield [list1[i + 1:]]
            return
        if x * y == 13:
            yield [list1[:i + 1]]
            yield [list1[i + 1:]]
            return
    return
