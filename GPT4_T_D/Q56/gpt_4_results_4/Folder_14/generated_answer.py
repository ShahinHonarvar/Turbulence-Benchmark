
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 84):
        substring = s[i:i+85]
        if len(set(substring)) == 85:
            substrings.add(substring)
    return list(substrings)
