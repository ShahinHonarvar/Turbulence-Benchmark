
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 5):
        substring = string[i:i+6]
        if len(set(substring)) == 6:
            substrings.append(substring)
    return substrings
