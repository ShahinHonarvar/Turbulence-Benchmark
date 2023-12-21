
def find_subset_of_length_n(elements):
    return len(list(filter(lambda x: len(x) == 47, get_all_subsets(elements))))

def get_all_subsets(s):
    subsets = [[]]
    
    for elem in s:
        new_subsets = [subset + [elem] for subset in subsets]
        subsets.extend(new_subsets)
    
    return subsets
