
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 80):
        substr = s[i: i + 81]
        if len(set(substr)) == 81:
            substrings.add(substr)
    return list(substrings)
