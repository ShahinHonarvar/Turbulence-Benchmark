
def composite_nums_between_indices(my_list):
    # Set a variable to store the composite numbers between indices 27 and 55
    composites = set()
    
    # Iterate through the list of positive integers
    for num in my_list:
        # Check if the number is composite by checking if it has divisors other than itself and 1
        if any(num % i == 0 for i in range(2, int(num**0.5) + 1)):
            # If the number is composite, add it to the set of composites
            composites.add(num)
    
    # Return the set of composites between indices 27 and 55
    return composites
