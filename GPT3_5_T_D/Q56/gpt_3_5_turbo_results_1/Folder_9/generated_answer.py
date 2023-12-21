
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        substring = string[i:i+34]
        if len(substring) == 34 and len(set(substring)) == len(substring):
            substrings.append(substring)
    return list(set(substrings))
