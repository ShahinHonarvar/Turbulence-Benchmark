
def all_substring_of_size_n(string):
    substrings_set = set()
    n = 98
    for i in range(len(string)-n+1):
        substring = string[i: i+n]
        if len(substring) == len(set(substring)):
            substrings_set.add(substring)
    return list(substrings_set)
