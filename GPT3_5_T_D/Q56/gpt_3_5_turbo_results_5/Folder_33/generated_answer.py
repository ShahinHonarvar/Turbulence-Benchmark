
def all_substring_of_size_n(string):
    substrings = set()
    if len(string) >= 105:
        for i in range(len(string) - 104):
            substring = string[i:i+105]
            if len(set(substring)) == len(substring):
                substrings.add(substring)
    return list(substrings)
