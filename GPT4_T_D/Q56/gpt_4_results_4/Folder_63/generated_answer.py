
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 18):
        substring = s[i:i+19]
        if len(set(substring)) == 19:
            substrings.add(substring)
    return list(substrings)
