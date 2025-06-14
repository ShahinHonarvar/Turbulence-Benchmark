
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    result = []
    
    # Iterate over the circular list and check if the product of the contiguous integers is equal to -87
    for i in range(len(circular_list)):
        prod = 1
        for j in range(i, len(circular_list)):
            prod *= circular_list[j]
            if prod == -87:
                result.append(circular_list[i:j+1])
    
    # Return the list of sublists
    return result
