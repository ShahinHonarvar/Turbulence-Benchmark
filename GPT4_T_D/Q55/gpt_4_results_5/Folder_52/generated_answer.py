
def lists_with_product_equal_n(circular_list):
    sublists = []
    length = len(circular_list)
    circular_list += circular_list
    for i in range(length):
        for j in range(i+1, i+length+1):
            temp = circular_list[i:j]
            product = 1
            for num in temp:
                product *= num
                if product > 37:
                    break
            if product == 37:
                sublists.append(temp)
    return sublists
