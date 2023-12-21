
def all_substring_of_size_n(string):
    substrings = []
    if len(string) >= 114:
        for i in range(len(string)-113):
            substring = string[i:i+114]
            if len(substring) == len(set(substring)):
                substrings.append(substring)
    return substrings
