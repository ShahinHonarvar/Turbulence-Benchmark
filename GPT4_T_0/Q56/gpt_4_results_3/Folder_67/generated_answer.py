
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 42):
        substring = s[i:i+43]
        if len(set(substring)) == 43:
            substrings.add(substring)
    return list(substrings)
