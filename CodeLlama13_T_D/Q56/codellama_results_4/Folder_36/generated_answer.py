
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 146 + 1):
        substring = s[i:i+146]
        if len(set(substring)) == 146 and not any(c*2 in substring for c in substring):
            substrings.append(substring)
    return substrings
