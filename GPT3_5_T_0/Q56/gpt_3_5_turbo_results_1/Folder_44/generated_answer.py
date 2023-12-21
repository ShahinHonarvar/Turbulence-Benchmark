
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 89):
        substring = string[i:i+90]
        if len(set(substring)) == 90:
            substrings.append(substring)
    return substrings
