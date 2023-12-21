
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 5):
        substring = s[i:i+6]
        if len(set(substring)) == 6:
            substrings.add(substring)
    return list(substrings)
