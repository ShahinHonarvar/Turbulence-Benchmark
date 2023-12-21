
def find_subset_of_length_n(elements):
    return len([subset for subset in powerset(elements) if len(subset) == 87])

def powerset(s):
    result = []
    for element in s:
        combinations = [x + [element] for x in result]
        result.extend(combinations)
    return result
