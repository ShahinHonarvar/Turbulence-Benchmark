
def all_substring_of_size_n(string):
    substrings = []
    
    if len(string) < 79:
        return substrings
    
    for i in range(len(string) - 78):
        substring = string[i:i+79]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    
    return substrings
