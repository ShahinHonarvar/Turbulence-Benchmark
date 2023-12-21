
def all_substring_of_size_n(s):
    substrings = set()
    len_s = len(s)
    
    for i in range(len_s):
        if i+10 <= len_s:
            substring = s[i:i+10]
            if len(substrings) == len(set(substrings)):
                substrings.add(substring)
                
    return list(substrings)
