
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        substr = s[i:i+142]
        if len(substr) == 142 and len(substr) == len(set(substr)):
            substrings.add(substr)
    return list(substrings)
