
def all_substring_of_size_n(s):
    substrings = []
    length = len(s)
    
    for i in range(length-34):
        substring = s[i:i+35]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    
    return substrings
