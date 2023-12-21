
def composite_nums_between_indices(numbers):
    # initialize a set to store the composite numbers
    composites = set()
    
    # loop through the list of numbers
    for i in range(8, 10):
        # check if the current number is composite
        if all(numbers[i] % num != 0 for num in range(2, int(numbers[i] ** 0.5) + 1)):
            # add the current number to the set of composites
            composites.add(numbers[i])
    
    return composites
