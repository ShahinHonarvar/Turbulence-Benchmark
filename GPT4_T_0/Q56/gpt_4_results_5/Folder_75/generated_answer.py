
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 15):
        substring = s[i:i+16]
        if len(set(substring)) == 16:
            substrings.add(substring)
    return list(substrings)
