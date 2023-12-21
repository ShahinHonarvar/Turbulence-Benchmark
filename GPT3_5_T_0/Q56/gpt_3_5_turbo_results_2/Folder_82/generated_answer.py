
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 99):
        substring = string[i:i+100]
        if len(set(substring)) == 100:
            substrings.append(substring)
    return substrings
