
def all_substring_of_size_n(string):
    substring_size = 39
    substrings = set()

    for i in range(len(string) - substring_size + 1):
        substring = string[i:i+substring_size]
        if len(set(substring)) == len(substring):
            substrings.add(substring)

    return list(substrings)
