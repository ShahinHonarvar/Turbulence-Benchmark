
def find_subset_of_length_n(elements):
    return len([sub for sub in powerset(elements) if len(sub) == 41])

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
