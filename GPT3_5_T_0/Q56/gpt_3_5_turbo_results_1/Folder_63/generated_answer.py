
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 18):
        substring = string[i:i+19]
        if len(set(substring)) == 19:
            substrings.append(substring)
    return substrings
