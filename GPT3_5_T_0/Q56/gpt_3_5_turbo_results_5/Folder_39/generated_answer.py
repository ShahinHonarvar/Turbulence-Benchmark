
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 93):
        substring = string[i:i+94]
        if len(set(substring)) == 94:
            substrings.append(substring)
    return substrings
