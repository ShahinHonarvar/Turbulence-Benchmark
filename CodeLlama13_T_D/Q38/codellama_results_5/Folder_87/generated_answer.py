
def find_subset_of_length_n(set_of_elements):
    return len([s for s in powerset(set_of_elements) if len(s) == 96])

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
