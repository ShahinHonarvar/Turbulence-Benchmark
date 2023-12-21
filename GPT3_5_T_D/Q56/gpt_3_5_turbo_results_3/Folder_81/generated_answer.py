
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 97):
        substring = string[i:i + 98]
        if len(set(substring)) == 98:
            substrings.append(substring)
    return substrings
