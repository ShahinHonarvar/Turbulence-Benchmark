
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        if len(string[i:i+11]) == 11 and len(set(string[i:i+11])) == 11:
            substrings.append(string[i:i+11])
    return list(set(substrings))
