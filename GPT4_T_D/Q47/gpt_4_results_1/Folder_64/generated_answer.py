
def palindromes_of_specific_lengths(in_string):
    import re
    in_string = re.sub('[^a-z]', '', in_string.lower())[:8]
    substrings = set()
    for i in range(len(in_string)):
        for j in range(i + 4, min(i + 6, len(in_string) + 1)):
            substring = in_string[i:j]
            if substring == substring[::-1]:
                substrings.add(substring)
    return substrings
