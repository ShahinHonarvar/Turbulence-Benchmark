
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-8):
        substring = string[i:i+9]
        if len(set(substring)) == 9:
            substrings.append(substring)
    return substrings
