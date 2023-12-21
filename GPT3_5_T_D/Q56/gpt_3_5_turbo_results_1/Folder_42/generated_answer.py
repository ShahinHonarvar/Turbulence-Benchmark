
def all_substring_of_size_n(string):
    substrings = []
    
    if len(string) < 45:
        return substrings
    
    for i in range(len(string) - 45 + 1):
        substring = string[i:i+45]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    
    return substrings
