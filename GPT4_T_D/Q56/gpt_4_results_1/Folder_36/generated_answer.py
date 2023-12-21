
def all_substring_of_size_n(s):
    substrings = set()
    if len(s) < 146:
        return []
    else:
        for i in range(len(s) - 145):
            substring = s[i:i+146]
            if len(set(substring)) == len(substring):
                substrings.add(substring)
    return list(substrings)
