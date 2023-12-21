
def find_subset_of_length_n(elements):
    return len([s for s in powerset(elements) if len(s) == 94])

def powerset(elements):
    return set(map(lambda x: frozenset(x), chain(*[combinations(elements, i+1) for i in range(len(elements)+1)])))
