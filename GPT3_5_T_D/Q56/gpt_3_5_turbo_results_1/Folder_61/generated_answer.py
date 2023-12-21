
def all_substring_of_size_n(string):
    substrings = []
    if len(string) >= 39:
        for i in range(len(string)-38):
            substring = string[i:i+39]
            if len(set(substring)) == len(substring):
                substrings.append(substring)
    return list(set(substrings))
