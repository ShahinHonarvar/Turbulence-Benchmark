
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 51):
        substring = s[i:i+52]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)
