
def all_substring_of_size_n(string):
    substrings = []
    
    if len(string) < 54:
        return substrings
    
    for i in range(len(string) - 53):  # Start index of substring
        substring = string[i:i+54]  # Extract substring of length 54
        
        if len(set(substring)) == 54:  # Check for no duplicate characters
            substrings.append(substring)
    
    return substrings
