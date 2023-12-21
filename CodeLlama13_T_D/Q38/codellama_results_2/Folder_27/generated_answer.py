
def find_subset_of_length_n(set):
    return len([subset for subset in powerset(set) if len(subset) == 56])

def powerset(s):
    ps = []
    for i in range(len(s)+1):
        ps.extend(list(combinations(s,i)))
    return ps
