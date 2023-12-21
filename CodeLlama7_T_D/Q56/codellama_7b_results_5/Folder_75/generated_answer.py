
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 16 + 1):
        substring = string[i:i+16]
        if len(substring) == 16 and not any(substring[j] in substrings for j in range(15)):
            substrings.append(substring)
    return substrings
