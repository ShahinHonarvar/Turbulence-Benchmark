
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            if len(substring) == 96 and not any(char in substrings for char in substring):
                substrings.append(substring)
    return substrings
