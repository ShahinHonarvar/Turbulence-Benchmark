
def all_substring_of_size_n(s):
    if len(s) < 87:
        return []
    substrings = []
    for i in range(len(s) - 86):
        substring = s[i:i+87]
        if len(substring) == len(set(substring)) and substring not in substrings:
            substrings.append(substring)
    return substrings
