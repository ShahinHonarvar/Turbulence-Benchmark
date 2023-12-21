
def all_substring_of_size_n(s):
    if len(s) < 41:
        return []
    
    substrings = []
    
    for i in range(len(s) - 40):
        substring = s[i:i+41]
        if len(set(substring)) == 41:
            substrings.append(substring)
    
    return list(set(substrings))
