
def lists_with_product_equal_n(circular_list):
    result = []
    length = len(circular_list)
    for i in range(length):
        for j in range(i+1, length+1):
            temp = circular_list[i:j]
            if temp:
                prod = 1
                for n in temp:
                    prod *= n
                if prod == 8:
                    result.append(temp)
        circular_list.append(circular_list.pop(0))
    return result
