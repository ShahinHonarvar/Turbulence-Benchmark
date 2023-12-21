
def all_substring_of_size_n(s):
    substrings = set()
    
    for i in range(len(s)):
        if len(s[i:i+130]) == 130 and len(set(s[i:i+130])) == 130:
            substrings.add(s[i:i+130])
            
    return list(substrings)
