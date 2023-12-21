
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 44):
        substring = s[i:i+45]
        if len(set(substring)) == 45:
            substrings.add(substring)
    return list(substrings)
