
def find_subset_of_length_n(elements, n):
    return len([subset for subset in powerset(elements) if len(subset) == n])

def powerset(elements):
    result = []
    for i in range(len(elements)):
        result.append(elements[i])
        result += [subset + (elements[i],) for subset in powerset(elements[i+1:])]
    return result
