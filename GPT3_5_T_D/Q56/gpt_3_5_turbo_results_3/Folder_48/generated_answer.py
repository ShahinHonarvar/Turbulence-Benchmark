
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 119):
        substring = string[i:i+120]
        if len(set(substring)) == 120:
            substrings.append(substring)
    return substrings
