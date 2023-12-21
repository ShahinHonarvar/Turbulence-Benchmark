
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 27):
        substring = string[i:i+28]
        if len(set(substring)) == 28:
            substrings.append(substring)
    return substrings
