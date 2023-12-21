
def all_substring_of_size_n(s):
    if len(s) < 12:
        return []
    
    substrings = []
    for i in range(len(s) - 11):
        substr = s[i:i+12]
        if len(substr) == len(set(substr)):
            if substr not in substrings:
                substrings.append(substr)
    
    return substrings
