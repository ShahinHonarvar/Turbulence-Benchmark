
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 67 + 1):
        substring = string[i:i+67]
        if len(set(substring)) == 68 and substring not in substrings:
            substrings.append(substring)
    return substrings
