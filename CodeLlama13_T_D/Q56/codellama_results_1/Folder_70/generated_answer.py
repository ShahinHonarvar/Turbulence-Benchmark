
def all_substring_of_size_n(string, n):
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[j-i:j] not in substrings and ''.join(sorted(string[j-i:j])) not in substrings:
                substrings.append(string[j-i:j])
    return substrings
