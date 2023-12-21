
def find_subset_of_length_n(elements, n):
    return len([subset for subset in powerset(elements) if len(subset) == n])

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
