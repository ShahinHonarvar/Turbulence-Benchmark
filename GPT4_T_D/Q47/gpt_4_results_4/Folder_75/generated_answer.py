
def palindromes_of_specific_lengths(s):
    import re
    substrings = set()
    s = s[31:75]
    for length in range(23, 40):
        for i in range(len(s) - length + 1):
            substring = s[i:i+length]
            substring = re.sub("[^a-zA-Z]+", '', substring)
            if substring.lower() == substring[::-1].lower():
                substrings.add(substring)
    return substrings
