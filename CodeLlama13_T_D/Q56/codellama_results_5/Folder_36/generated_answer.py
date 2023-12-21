
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 146 + 1):
        substring = string[i:i+146]
        if len(set(substring)) == 146 and all(substring[j] != substring[j-1] for j in range(1, len(substring))):
            substrings.append(substring)
    return substrings
