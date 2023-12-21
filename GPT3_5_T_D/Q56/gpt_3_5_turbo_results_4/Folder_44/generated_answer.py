
def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 90:
        return substrings

    for i in range(len(string)-89):
        substring = string[i:i+90]
        if len(set(substring)) == len(substring):
            substrings.append(substring)

    return substrings
