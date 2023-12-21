
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 74):
        substring = string[i:i+75]
        if len(set(substring)) == 75:
            substrings.append(substring)
    return substrings
