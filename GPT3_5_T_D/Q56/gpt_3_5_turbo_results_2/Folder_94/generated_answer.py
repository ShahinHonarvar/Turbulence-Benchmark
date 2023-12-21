
def all_substring_of_size_n(string):
    substrings = []
    if len(string) >= 70:
        for i in range(len(string)-69):
            substring = string[i:i+70]
            if len(set(substring)) == 70:
                substrings.append(substring)
    return substrings
