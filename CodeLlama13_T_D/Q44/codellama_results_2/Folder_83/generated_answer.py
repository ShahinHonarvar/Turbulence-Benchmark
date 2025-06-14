
def composite_nums_between_indices(my_list):
    # Set of all composite numbers between index 111 and index 111, both inclusive
    composites = set()
    
    # Iterate through the list
    for i in range(111, 112):
        # Check if the current element is a composite number
        if my_list[i] > 1:
            # Add it to the set of composites
            composites.add(my_list[i])
    
    return composites
