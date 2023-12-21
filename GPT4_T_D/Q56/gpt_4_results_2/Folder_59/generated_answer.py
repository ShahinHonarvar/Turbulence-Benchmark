
def all_substring_of_size_n(s):
    n = 77
    substrings = set()
    for i in range(len(s)):
        if i+n > len(s): 
            break
        substr = s[i:i+n]
        if len(set(substr)) == n:
            substrings.add(substr)
    return list(substrings)
