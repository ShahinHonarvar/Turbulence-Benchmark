
def find_subset_of_length_n(set_of_elements, n):
    subsets = 0
    for subset in power_set(set_of_elements):
        if len(subset) == n:
            subsets += 1
    return subsets

def power_set(s):
    result = [[]]
    for e in s:
        result.extend([[e]+subset for subset in result])
    return result
