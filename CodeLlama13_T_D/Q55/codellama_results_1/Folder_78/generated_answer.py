
def lists_with_product_equal_n(circular_list):
    # Initialize an empty list to store the sublists
    sublists = []
    
    # Iterate through the circular list
    for i in range(len(circular_list)):
        # Initialize a product variable to store the product of integers in the current sublist
        prod = 1
        
        # Iterate through the current sublist
        for j in range(i, len(circular_list)):
            # Multiply the product by the current integer
            prod *= circular_list[j]
            
            # If the product is equal to n, add the sublist to the list of sublists
            if prod == 74:
                sublists.append(circular_list[i:j+1])
                
            # Break out of the inner loop if the product is greater than n
            elif prod > 74:
                break
    
    return sublists
