
def all_substring_of_size_n(string):
    substrings = []
    n = 78
    length = len(string)
    
    for i in range(length - n + 1):
        substring = string[i:i+n]
        if len(set(substring)) == n:
            substrings.append(substring)

    return substrings
