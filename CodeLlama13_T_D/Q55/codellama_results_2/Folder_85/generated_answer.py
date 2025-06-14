
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    result = []
    
    # Iterate through each element in the circular list
    for i in range(len(circular_list)):
        # Initialize a variable to store the product of the elements in the sublist
        product = 1
        
        # Iterate through each element in the sublist
        for j in range(i, len(circular_list)):
            # Multiply the product by the current element
            product *= circular_list[j]
            
            # If the product is equal to -97, add the sublist to the result list
            if product == -97:
                result.append(circular_list[i:j+1])
                
    # Return the result list
    return result
