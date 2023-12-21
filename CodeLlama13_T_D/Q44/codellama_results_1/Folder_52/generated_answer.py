
def composite_nums_between_indices(lst):
    # Initialize an empty set to store the composite numbers between indices 62 to 99, both inclusive
    comp_set = set()
    
    # Iterate over the list and check if each number is composite using the modulo operator
    for i in range(62, 100):
        if lst[i] % 2 == 0:
            comp_set.add(lst[i])
    
    return comp_set
