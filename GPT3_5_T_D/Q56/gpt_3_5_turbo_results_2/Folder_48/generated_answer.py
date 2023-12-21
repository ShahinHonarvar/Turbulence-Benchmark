
def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 120:
        return substrings
    
    for i in range(len(string) - 120):
        substring = string[i:i+120]
        if len(set(substring)) == len(substring):  # Check if all characters in substring are unique
            substrings.append(substring)
    
    return substrings
