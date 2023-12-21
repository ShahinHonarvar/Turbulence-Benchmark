
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 94):
        if len(set(string[i:i+94])) == 94:
            substrings.append(string[i:i+94])
    return substrings
