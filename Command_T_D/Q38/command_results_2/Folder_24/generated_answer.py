def find_subset_of_length_n(set_of_elements):
    n = 74
    result = 0
    for element in set_of_elements:
        result += 1**n
        n -= 1
    return result
