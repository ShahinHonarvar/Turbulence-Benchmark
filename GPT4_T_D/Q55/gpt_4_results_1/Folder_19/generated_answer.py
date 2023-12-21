
def lists_with_product_equal_n(circular_list):
    lst, length, sublists = list(circular_list), len(circular_list), []
    extended_lst = lst + lst  #replicate the circle by appending the list to itself
    for i in range(length): 
       product = 1
       for j in range(i, length + i):
           product *= extended_lst[j]
           if product == -54:
               sublists.append(extended_lst[i:j + 1])
    return sublists
