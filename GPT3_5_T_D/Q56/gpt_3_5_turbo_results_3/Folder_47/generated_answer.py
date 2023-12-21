
def all_substring_of_size_n(string):
    substrings = []
    length = len(string)

    if length < 91:
        return substrings

    for i in range(length - 91 + 1):
        substring = string[i:i+91]
        if len(set(substring)) == 91:
            substrings.append(substring)

    return substrings
