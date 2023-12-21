
def all_substring_of_size_n(str):
    substrings = []
    for i in range(len(str) - 43):
        substring = str[i:i+44]
        if len(set(substring)) == len(substring):
            if substring not in substrings:
                substrings.append(substring)
    return substrings
