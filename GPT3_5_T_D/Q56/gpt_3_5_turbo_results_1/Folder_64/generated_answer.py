
def all_substring_of_size_n(s):
    substrings = []
    
    if len(s) < 8:
        return substrings
    
    for i in range(len(s)-7):
        substring = s[i:i+8]
        if len(set(substring)) == 8:
            substrings.append(substring)
    
    return substrings
