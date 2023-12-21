 
def find_subset_of_length_n(elements):
    return len(elements) * (len(elements) - 1) * (len(elements) - 2) * (len(elements) - 3) // 24
