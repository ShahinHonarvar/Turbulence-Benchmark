
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if len(set(s[i:i+87])) == 87:
            substrings.add(s[i:i+87])
    return list(substrings)
