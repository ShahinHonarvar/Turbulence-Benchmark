def find_subset_of_length_n(set_of_elements):
    result = 1
    for element in set_of_elements:
        result *= set_of_elements.count(element)
    return result
