
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 96):
        substring = string[i:i+97]
        if len(set(substring)) == len(substring):
            if substring not in substrings:
                substrings.append(substring)
    return substrings
