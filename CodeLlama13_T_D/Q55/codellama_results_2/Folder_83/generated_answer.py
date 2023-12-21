
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    result = []
    
    # Iterate through each element in the circular list
    for i in range(len(circular_list)):
        # Calculate the product of the current element and all subsequent elements
        product = 1
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            
            # If the product is equal to -57, add the sublist to the result list
            if product == -57:
                result.append(circular_list[i:j+1])
    
    return result
