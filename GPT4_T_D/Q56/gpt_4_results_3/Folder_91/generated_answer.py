
def all_substring_of_size_n(s):
    substrings = set()

    for i in range(len(s)):
        if len(s[i:i+6]) == 6 and len(set(s[i:i+6])) == 6:
            substrings.add(s[i:i+6])
    
    return list(substrings)
