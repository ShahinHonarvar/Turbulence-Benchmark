
def all_substring_of_size_n(string):
    substrings = []
    n = 88
    length = len(string)
    
    for i in range(length - n + 1):
        substring = string[i:i+n]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    
    return substrings
