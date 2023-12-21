
def composite_nums_between_indices(lst):
    # Create a set to store the composite numbers
    composites = set()
    
    # Iterate through the list and check if each number is composite
    for i in range(62, 63 + 1):
        if lst[i] > 1 and lst[i] % lst[i - 1] == 0:
            composites.add(lst[i])
    
    # Return the set of composite numbers between indices 62 to 63, both inclusive
    return composites
