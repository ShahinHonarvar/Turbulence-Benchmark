
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 40):
        substring = s[i:i+41]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)
