
def all_substring_of_size_n(string):
    size = 26
    substrings = []
    
    for i in range(len(string)):
        substring = string[i:i+size]
        if len(substring) == size and len(set(substring)) == size:
            substrings.append(substring)
    
    return substrings
