
def all_substring_of_size_n(string):
    substrings = []
    n = 67
    length = len(string)
  
    if length >= n:
        for i in range(length - n + 1):
            substring = string[i:i+n]
            if len(set(substring)) == len(substring):
                substrings.append(substring)
  
    return substrings
