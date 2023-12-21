
def all_substrings_of_size_n(string):
    substrings = []
    if len(string) >= 47:
        for i in range(len(string) - 46):
            substring = string[i:i+47]
            if len(set(substring)) == 47:
                substrings.append(substring)
    return substrings
