
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if i + 29 > len(s):
            break
        substr = s[i:i+29]
        if len(set(substr)) == len(substr):
            substrings.add(substr)
    return list(substrings)
