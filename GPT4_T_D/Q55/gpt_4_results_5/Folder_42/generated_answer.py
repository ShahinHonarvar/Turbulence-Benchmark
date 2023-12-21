
def lists_with_product_equal_n(lst):
    num_elements = len(lst)
    lst = lst*2
    result = []

    for i in range(num_elements):
        for j in range(i+1, num_elements+i+1):
            sublist = lst[i:j]
            mult = 1
            for num in sublist:
                mult *= num

            if mult == 25:
                if sublist not in result:
                    result.append(sublist)
                    
    return result
