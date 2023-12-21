
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 38):
        substring = string[i:i+39]
        if len(set(substring)) == 39 and substring not in substrings:
            substrings.append(substring)
    return substrings
