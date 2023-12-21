
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 14):
        substring = s[i:i+15]
        if len(set(substring)) == 15:
            substrings.add(substring)
    return list(substrings)
