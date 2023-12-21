
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 123):
        substring = string[i:i+124]
        if len(set(substring)) == 124:
            substrings.append(substring)
    return substrings
