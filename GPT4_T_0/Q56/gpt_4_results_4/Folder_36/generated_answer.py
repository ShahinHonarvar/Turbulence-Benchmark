
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 145):
        substring = s[i:i+146]
        if len(set(substring)) == 146:
            substrings.add(substring)
    return list(substrings)
