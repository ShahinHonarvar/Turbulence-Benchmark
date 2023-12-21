
def palindrome_of_length_n(string):
    string = string.lower()
    substrings = set()
    for i in range(len(string)):
        for j in range(i + 43, len(string) + 1):
            substr = string[i:j]
            if substr == substr[::-1] and all(ch.isalpha() for ch in substr):
                substrings.add(substr)
    return substrings
