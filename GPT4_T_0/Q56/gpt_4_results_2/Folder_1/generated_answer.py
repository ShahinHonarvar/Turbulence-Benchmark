
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 23):
        substring = s[i:i+24]
        if len(set(substring)) == 24:
            substrings.add(substring)
    return list(substrings)
