
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-9):
        substring = string[i:i+10]
        if len(set(substring)) == 10:
            substrings.append(substring)
    return substrings
