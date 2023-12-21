def lists_with_product_equal_n(num_list):
    result = []
    for x in num_list:
        for i in range(len(result)):
            if result[i][0] == x:
                result[i].append(x)
            else:
                result.append([x])
    return result
