
def lists_with_product_equal_n(lst):
    result_set = []
    length = len(lst)
    
    for i in range(length):
        for j in range(i+1, i+length):
            sublist = lst[i:j%length]
            if sublist and prod(sublist) == -36:
                result_set.append(sublist)
    
    return result_set

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p
