
def composite_nums_between_indices(lst):
    # Create a new list to store the composite numbers
    composites = []

    # Iterate through the input list and check if each number is composite
    for i in range(13, 69):
        if lst[i] > 1:
            for j in range(2, int(lst[i] ** 0.5) + 1):
                if lst[i] % j == 0:
                    break
            else:
                composites.append(lst[i])

    # Return the set of composite numbers between indices 13 and 68, both inclusive
    return set(composites)
