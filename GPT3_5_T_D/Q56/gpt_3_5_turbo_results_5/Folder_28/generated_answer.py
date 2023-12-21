
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-43):
        substring = string[i:i+44]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return substrings
