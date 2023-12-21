def find_subset_of_length_n(set_of_elements):
    # Take a look at: http://www.xaprb.com/blog/2013/10/13/efficient- calculation-of-permutations-in-/
    return len(set_of_elements) ** (len(set_of_elements) - 1) // (2 ** (len(set_of_elements) - 1))
