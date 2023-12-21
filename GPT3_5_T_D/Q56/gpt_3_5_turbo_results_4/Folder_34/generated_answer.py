
def all_substring_of_size_n(string):
    substrings = []
    
    for i in range(len(string)):
        if i+84 <= len(string):
            substring = string[i:i+84]
            if len(set(substring)) == len(substring):
                substrings.append(substring)
    
    return list(set(substrings))
