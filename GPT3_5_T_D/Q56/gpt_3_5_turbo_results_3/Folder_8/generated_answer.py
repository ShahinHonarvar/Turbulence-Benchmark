
def all_substring_of_size_n(string):
    substrings = []
    size = 30
    length = len(string)
    
    if length < size:
        return substrings
    
    for i in range(length - size + 1):
        substring = string[i:i+size]
        if len(set(substring)) == size:
            substrings.append(substring)
    
    return substrings
