
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 95 + 1):
        substring = s[i:i+95]
        if len(set(substring)) == 95:
            substrings.append(substring)
    return substrings
