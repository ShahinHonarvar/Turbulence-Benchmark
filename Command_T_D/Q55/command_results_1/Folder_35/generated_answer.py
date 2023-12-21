def lists_with_product_equal_n(list1):
    result = []
    for i in range(len(list1)):
        j = 0
        while j < len(list1) - 1:
            if list1[i] * list1[j] * list1[j + 1] == 83:
                result.append([list1[i], list1[j], list1[j + 1]])
            j += 1
    return result
