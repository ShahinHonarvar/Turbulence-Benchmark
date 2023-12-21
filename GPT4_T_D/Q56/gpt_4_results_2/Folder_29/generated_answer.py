
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 94):
        substring = s[i:i+95]
        if len(set(substring)) == 95:
            substrings.add(substring)
    return list(substrings)
