
def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 91:
        return substrings
    for i in range(len(string)-90):
        substring = string[i:i+91]
        if len(set(substring)) == 91:
            substrings.append(substring)
    return substrings
