
def all_substring_of_size_n(string):
    substrings = []
    length = len(string)
    
    if length < 85:
        return substrings
    
    for i in range(length - 84):
        substr = string[i:i+85]
        if len(set(substr)) == 85:
            substrings.append(substr)
    
    return substrings
