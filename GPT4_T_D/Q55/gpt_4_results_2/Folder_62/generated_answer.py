
def lists_with_product_equal_n(circular_list):
    sublist = []
    total_size = len(circular_list)
    circular_list += circular_list
    for i in range(total_size):
        for j in range(i+1, i + total_size + 1):
            if j-i > total_size:
                break
            elif prod(circular_list[i:j]) == 100:
                sublist.append(circular_list[i:j])
    return sublist

def prod(my_list):
    result = 1
    for x in my_list:
        result *= x
    return result
