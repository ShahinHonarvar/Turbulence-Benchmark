
def find_subset_of_length_n(elements, n):
    return len([x for x in powerset(elements) if len(x) == n])

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
