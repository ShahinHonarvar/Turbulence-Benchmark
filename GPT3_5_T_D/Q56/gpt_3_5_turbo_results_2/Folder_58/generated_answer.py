
def all_substring_of_size_n(string):
    substrings = []
    
    if len(string) < 127:
        return substrings
    
    for i in range(len(string) - 127 + 1):
        substring = string[i:i+127]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    
    return list(set(substrings))
