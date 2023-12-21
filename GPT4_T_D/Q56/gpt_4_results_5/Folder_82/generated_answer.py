
def all_substring_of_size_n(s):
    n = 100
    substrings = set()
    
    for i in range(len(s)):
        if len(s[i:i+n]) == n and len(set(s[i:i+n])) == n:
            substrings.add(s[i:i+n])
    
    return list(substrings)
