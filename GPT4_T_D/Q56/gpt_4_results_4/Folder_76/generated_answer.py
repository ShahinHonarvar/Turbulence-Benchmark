
def all_substring_of_size_n(s):
    substrings = set()
    length = len(s)
    for i in range(length - 148):
        substring = s[i:i+149]
        if len(set(substring)) == 149:
            substrings.add(substring)
    return list(substrings)
