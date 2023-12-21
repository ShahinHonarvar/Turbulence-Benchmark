
def all_substring_of_size_n(string):
    substrings = []
    length = len(string)
    if length < 19:
        return substrings
    
    for i in range(length - 18):
        substring = string[i:i+19]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    
    return substrings
