
def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 64:
        return substrings
    
    for i in range(len(string) - 63):
        substring = string[i:i+64]
        if len(set(substring)) == 64:
            substrings.append(substring)
    
    return substrings
