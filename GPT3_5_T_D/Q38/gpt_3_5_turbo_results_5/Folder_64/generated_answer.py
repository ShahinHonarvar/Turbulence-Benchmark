
def find_subset_of_length_n(elements):
    if not isinstance(elements, set):
        return None
    count = 0
    for element in elements:
        count += 1
    return count
