def lists_with_product_equal_n(list):
    lists = []
    for i in range(1, len(list) + 1):
        if list[i - 1] * i == 27:
            lists.append(list[i - 1:i + 1])
    return lists
