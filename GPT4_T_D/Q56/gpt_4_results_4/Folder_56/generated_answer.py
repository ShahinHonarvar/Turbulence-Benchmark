
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 68):
        substring = s[i:i+69]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)
