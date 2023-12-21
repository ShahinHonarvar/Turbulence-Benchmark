
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 62):
        substring = string[i:i+63]
        if len(set(substring)) == 63:
            substrings.append(substring)
    return substrings
