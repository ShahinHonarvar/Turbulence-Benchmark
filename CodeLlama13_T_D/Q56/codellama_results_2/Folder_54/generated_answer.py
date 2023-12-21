
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 28 + 1):
        substring = string[i:i+28]
        if len(set(substring)) == 28 and not any(substring[j] in substring[:j] for j in range(1, len(substring))):
            substrings.append(substring)
    return substrings
