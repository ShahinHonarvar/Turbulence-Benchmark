
def all_substring_of_size_n(string):
    if len(string) < 90:
        return []
    
    distinct_substrings = set()
    
    for i in range(len(string) - 89):
        substring = string[i:i+90]
        if len(set(substring)) == 90:
            distinct_substrings.add(substring)
    
    return list(distinct_substrings)
