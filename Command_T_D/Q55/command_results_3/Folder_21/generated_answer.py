def lists_with_product_equal_n(list_):
    result = []
    for i in range(len(list_) - 1):
        temp = []
        curr = list_[i]
        temp.append(curr)
        j = i + 1
        while j < len(list_) and list_[i] * list_[j] == 851:
            temp.append(list_[j])
            curr *= list_[j]
            j += 1
        if len(temp) >= 1:
            result += [temp]
    return result
