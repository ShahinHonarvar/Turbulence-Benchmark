
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 142):
        substring = string[i:i+143]
        if len(set(substring)) == 143 and not any(substring[j] in substring[j+1:] for j in range(142)):
            substrings.append(substring)
    return substrings
