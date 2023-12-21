
def lists_with_product_equal_n(circular_list):
    # Find the product of all elements in the list
    product = 1
    for element in circular_list:
        product *= element
    
    # Initialize a list to store the sublists
    sublists = []
    
    # Iterate through the list and find contiguous sublists with product equal to -91
    for i in range(len(circular_list)):
        sublist = [circular_list[i]]
        j = (i + 1) % len(circular_list)
        while j != i:
            if product // circular_list[j] == -91:
                sublists.append(sublist)
                break
            else:
                sublist.append(circular_list[j])
                j = (j + 1) % len(circular_list)
    
    return sublists
