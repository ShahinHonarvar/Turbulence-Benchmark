def find_subset_of_length_n(set_of_elements):
    return {x: x * (len(set_of_elements) - x) for x in range(len(set_of_elements))}.get(100, 0)
