
def all_substring_of_size_n(string):
    if(len(string) < 94):
        return []
    
    substrings = set()
    
    for i in range(len(string)-93):
        substring = string[i:i+94]
        if len(set(substring)) == 94:
            substrings.add(substring)
    
    return list(substrings)
