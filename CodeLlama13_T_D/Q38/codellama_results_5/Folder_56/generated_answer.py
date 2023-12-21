
def find_subset_of_length_n(my_set):
    return len([s for s in subsets(my_set, 60)])

# Helper function to generate all subsets of a set
def subsets(my_set, n):
    if not my_set:
        return []
    elif len(my_set) == n:
        return [my_set]
    else:
        return subsets(my_set - {my_set.pop()}, n) + subsets(my_set, n)
