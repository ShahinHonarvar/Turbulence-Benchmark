
def lists_with_product_equal_n(lst):
    num_list, len_lst, result = lst + lst, len(lst), []
    for i in range(len_lst):
        for size in range(1, len_lst+1):
            prod = 1
            for j in range(i, i+size):
                prod *= num_list[j]
                if prod > 851:
                    break
            if prod == 851:
                result.append(num_list[i:i+size])
    return result
