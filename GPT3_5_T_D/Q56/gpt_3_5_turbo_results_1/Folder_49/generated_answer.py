

def all_substring_of_size_n(string):
    substring_set = set()
    n = 73
    
    if len(string) < n:
        return []
    
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if len(set(substring)) == n:
            substring_set.add(substring)
    
    return list(substring_set)
