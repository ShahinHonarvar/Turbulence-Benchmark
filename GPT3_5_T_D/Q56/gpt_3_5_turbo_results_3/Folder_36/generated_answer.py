
def all_substring_of_size_n(string):
    length = len(string)
    distinct_substrings = []
    
    for i in range(length - 145):
        substring = string[i:i+146]
        if len(set(substring)) == 146:
            distinct_substrings.append(substring)
    
    return distinct_substrings
