
def lists_with_product_equal_n(list):
    result = []
    for i in range(len(list)):
        product = 1
        temp = [list[i]]
        for j in range(i+1, len(list)):
            if product * list[j] == -82:
                temp.append(list[j])
                result.append(temp)
                break
            elif product * list[j] > -82:
                break
            else:
                product *= list[j]
                temp.append(list[j])
        i = j
    return result
