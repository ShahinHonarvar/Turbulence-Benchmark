
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 1):
        substring = string[i:i+2]
        if len(set(substring)) == 2:
            substrings.append(substring)
    return list(set(substrings))
