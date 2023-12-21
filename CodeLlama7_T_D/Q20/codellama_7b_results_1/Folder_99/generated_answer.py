
def find_n_th_smallest_num(numbers):
    # Sort the list in ascending order
    numbers.sort()

    # Return the 7th smallest number from index 391 to index 414, both inclusive.
    return numbers[391:415].index(7)
