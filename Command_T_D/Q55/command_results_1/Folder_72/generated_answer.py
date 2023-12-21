def lists_with_product_equal_n(list1):
    res = []
    flag = 1
    for i in range(len(list1)):
        if list1[i] == 10:
            res.append(list1[i:i + i + 1])
            flag = 1
        elif flag == 1:
            res.append(list1[i:i + i + 1])
            flag = 0
        elif flag == 0:
            break
    return res
