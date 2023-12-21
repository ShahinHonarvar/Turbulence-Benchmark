
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 86):
        substring = string[i:i+87]
        if len(set(substring)) == 87:
            substrings.append(substring)
    return substrings
