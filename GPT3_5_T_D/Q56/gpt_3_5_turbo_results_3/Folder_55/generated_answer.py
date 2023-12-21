
def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 40:
        return substrings
    
    for i in range(len(string)-39):
        substring = string[i:i+40]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    
    return substrings
