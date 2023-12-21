
def all_substring_of_size_n(string):
    if len(string) < 86:
        return []
        
    substrings = set()
    for i in range(len(string)-85):
        substring = string[i:i+86]
        if len(set(substring)) == 86:
            substrings.add(substring)
        
    return list(substrings)
