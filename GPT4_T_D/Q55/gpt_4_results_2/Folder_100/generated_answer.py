
def lists_with_product_equal_n(circular_list):
    list_length = len(circular_list)
    results = []
    circular_list += circular_list 

    for i in range(list_length):
        for j in range(i + 1, i + list_length + 1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if (product == 48):
                results.append(sublist)
                
    return results
