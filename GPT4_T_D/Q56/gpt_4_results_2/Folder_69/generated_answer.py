
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 98):
        if len(set(s[i:i+99])) == 99:
            substrings.add(s[i:i+99])
    return list(substrings)
