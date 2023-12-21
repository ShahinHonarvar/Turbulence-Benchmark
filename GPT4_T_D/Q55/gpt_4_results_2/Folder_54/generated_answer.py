
def lists_with_product_equal_n(circular_list):
    sublist_products = [1]
    sublists = [[circular_list[0]]]
    result = []
    
    # Generating sublists and their products 
    for i in range(1, len(circular_list)):
        sublist_products = [circular_list[i]] + [circular_list[i]*product for product in sublist_products]
        sublists = [[circular_list[i]]] + [sublist + [circular_list[i]] for sublist in sublists]
    
    # Handling the circularity by testing sublists from tail to head
    for num in reversed(circular_list[:-1]):
        new_sublist_products = [num * product for product in sublist_products]
        new_sublists = [sublist + [num] for sublist in sublists]
        sublist_products += new_sublist_products
        sublists += new_sublists

    # Checking for sublists with product equal to -17 and storing them in result
    for i in range(len(sublist_products)):
        if sublist_products[i] == -17:
            result.append(sublists[i])
    return result
