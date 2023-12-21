
def all_even_ints_exclusive(my_list):
    # Get the range of even integers
    start = 598
    end = 767
    # Create an empty list to store the results
    results = []

    # Iterate through the list and append even integers to the results list
    for i in range(start, end):
        if my_list[i] % 2 == 0:
            results.append(my_list[i])

    return results
