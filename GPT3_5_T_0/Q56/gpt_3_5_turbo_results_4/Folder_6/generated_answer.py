
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 22):
        substring = string[i:i+23]
        if len(set(substring)) == 23:
            substrings.append(substring)
    return substrings
