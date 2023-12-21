
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 53):
        subset = s[i:i+54]
        if len(set(subset)) == len(subset):
            substrings.add(subset)
    return list(substrings)
