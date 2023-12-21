
def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    circular_list = circular_list * 2
    sublists = []

    for i in range(size):
        for j in range(i+1, i+size+1):
            sub_list = circular_list[i:j]
            product = 1
            for num in sub_list:
                product *= num
            if product == -76:
                sublists.append(sub_list)
    
    return sublists
