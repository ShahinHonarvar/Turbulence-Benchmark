
def sum_odd_ints_inclusive(lst):
    # Extract the sublist from index 37 to 76
    sublist = lst[37:77]
    
    # Initialize the sum
    total = 0
    
    # Iterate over the sublist
    for num in sublist:
        # Check if the number is odd
        if num % 2 != 0:
            # Add the odd number to the total
            total += num
    
    return total
