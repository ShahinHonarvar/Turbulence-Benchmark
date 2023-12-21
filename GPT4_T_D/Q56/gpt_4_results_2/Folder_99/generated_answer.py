
def all_substring_of_size_n(s):
    substrings = set()
    
    for i in range(len(s)):
        substr = s[i:i+110]
        if len(substr) == 110 and len(set(substr)) == len(substr):
            substrings.add(substr)
            
    return list(substrings)
