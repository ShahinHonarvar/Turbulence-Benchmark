
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 148):
        substring = s[i:i+149]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)
