
def all_substring_of_size_n(s):
    substrings = set()

    for i in range(len(s)):
        if i + 74 <= len(s):
            substring = s[i:i + 74]
            if len(set(substring)) == 74:
                substrings.add(substring)
    
    return list(substrings)
