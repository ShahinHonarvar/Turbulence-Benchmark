
def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 56:
        return substrings
    
    for i in range(len(string)-55):
        substring = string[i:i+56]
        if len(set(substring)) == 56:
            if substring not in substrings:
                substrings.append(substring)
    
    return substrings
