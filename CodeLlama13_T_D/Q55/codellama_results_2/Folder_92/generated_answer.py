
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    result = []
    
    # Iterate over each element in the circular list
    for i in range(len(circular_list)):
        # Initialize a product variable to store the product of elements in the current sublist
        product = 1
        
        # Iterate over each element in the circular list, starting from the current index
        for j in range(i, len(circular_list) + i):
            # Calculate the product of elements in the current sublist
            product *= circular_list[j % len(circular_list)]
            
            # If the product is equal to 5, add the current sublist to the result list
            if product == 5:
                result.append(circular_list[i:j + 1])
                
    # Return the result list
    return result
