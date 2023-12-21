
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            substring = string[i:j]
            if len(substring) == 114 and all(char not in substring for char in substring):
                substrings.append(substring)
    return list(set(substrings))
