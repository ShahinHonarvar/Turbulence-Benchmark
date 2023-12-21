
def all_substring_of_size_n(s):
    substring_length = 105
    all_substrings = set()
    
    for i in range(len(s) - substring_length + 1):
        substring = s[i:i+substring_length]
        if len(set(substring)) == len(substring):
            all_substrings.add(substring)
            
    return list(all_substrings)
