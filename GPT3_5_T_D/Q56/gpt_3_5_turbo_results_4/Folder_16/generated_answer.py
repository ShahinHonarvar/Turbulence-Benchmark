
def all_substring_of_size_n(string):
    substrings = []
    length = len(string)
    unique_length = 124
    
    if length < unique_length:
        return substrings
    
    for i in range(length - unique_length + 1):
        substring = string[i:i + unique_length]
        if len(set(substring)) == unique_length:
            substrings.append(substring)
    
    return substrings
