
def find_subset_of_length_n(elements, n):
    # Initialize a list to store all subsets of size n
    subsets = []
    
    # Iterate over each element in the set
    for element in elements:
        # If the current subset is not of size n, add the current element to it
        if len(subsets) < n:
            subsets.append([element])
        else:
            # If the current subset is of size n, find all subsets of size n - 1 that do not contain the current element
            for i in range(len(subsets)):
                if element not in subsets[i]:
                    subsets[i].append(element)
    
    # Return the number of all subsets of size n
    return len(subsets)
