
def lists_with_product_equal_n(circle):
    n = len(circle) # Length of the circular list
    sublists = [] # List to store sublists

    for i in range(n): # Iterate over each element in the circular list
        product = 1 # Initialize product as 1
        
        for j in range(i, i + n): # Iterate over a window of size 'n'
            product *= circle[j % n] # Calculate product for each sublist
            
            if product == -75: # If product equals -75, add sublist to the result list
                sublist = circle[i:(j % n) + 1]
                sublists.append(sublist)

    return sublists
