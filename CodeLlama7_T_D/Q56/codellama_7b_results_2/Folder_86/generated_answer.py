
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 143 + 1):
        substring = string[i:i+143]
        if len(substring) == 143 and not any(substring[j+1:] in substring[0:j] for j in range(142)):
            substrings.append(substring)
    return substrings
