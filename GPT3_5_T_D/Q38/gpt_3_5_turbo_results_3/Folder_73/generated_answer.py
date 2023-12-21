
def find_subset_of_length_n(elements):
    return len(list(filter(lambda x: len(x) == 41, subsets(elements))))

def subsets(elements):
    if not elements:
        return [[]]
    subsets_without_first_element = subsets(elements[1:])
    subsets_with_first_element = [[elements[0]] + subset for subset in subsets_without_first_element]
    return subsets_without_first_element + subsets_with_first_element
