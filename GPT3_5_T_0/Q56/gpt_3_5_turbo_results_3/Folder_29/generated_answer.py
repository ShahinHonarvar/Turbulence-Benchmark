
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 94):
        substring = string[i:i+95]
        if len(set(substring)) == 95:
            substrings.append(substring)
    return substrings
