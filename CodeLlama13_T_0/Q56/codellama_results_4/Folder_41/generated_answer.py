
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 73):
        substring = s[i:i+74]
        if len(set(substring)) == 74 and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
