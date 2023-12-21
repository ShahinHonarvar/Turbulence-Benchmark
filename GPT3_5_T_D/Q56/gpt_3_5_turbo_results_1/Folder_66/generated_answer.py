
def all_substring_of_size_n(s):
    substrings = []
    n = len(s)
    if n < 26:
        return substrings
    
    for i in range(n - 25):
        substring = s[i:i+26]
        if len(set(substring)) == 26:
            substrings.append(substring)
    
    return substrings
