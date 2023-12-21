
def all_substring_of_size_n(string):
    substrings = []
    length = len(string)
    if length < 81:
        return []
    for i in range(length - 80):
        substr = string[i:i+81]
        if len(set(substr)) == len(substr):
            substrings.append(substr)
    return substrings
