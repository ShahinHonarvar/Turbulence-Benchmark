
def all_substring_of_size_n(string):
    substrings = []
    length = 6
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings
