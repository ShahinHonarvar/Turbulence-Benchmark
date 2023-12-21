
def all_substring_of_size_n(string):
    if len(string) < 45:
        return []
    
    substrings = set()
    for i in range(len(string)-44):
        substring = string[i:i+45]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    
    return list(substrings)
