
def all_substring_of_size_n(s):
    substrings = set()
    n = len(s)
    if n < 35:
        return []
    
    for i in range(n-34):
        substring = s[i:i+35]
        if len(set(substring)) == 35:
            substrings.add(substring)
    
    return list(substrings)
