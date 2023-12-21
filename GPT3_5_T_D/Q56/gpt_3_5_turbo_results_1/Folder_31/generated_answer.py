
def all_substring_of_size_n(string):
    if len(string) < 46:
        return []
    
    substrings = set()
    for i in range(len(string) - 45):
        substring = string[i:i+46]
        if len(set(substring)) == 46:
            substrings.add(substring)
    
    return list(substrings)
