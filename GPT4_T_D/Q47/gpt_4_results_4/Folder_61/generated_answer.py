
def palindromes_of_specific_lengths(string):
    import re
    string = string[0:31]
    patterns = set()
    low_case_string = string.lower()
    for length in range(20, 31):
        for i in range(len(low_case_string) - length + 1):
            sub = low_case_string[i:i+length]
            if sub == sub[::-1] and re.match("^[a-z]*$", sub):
                patterns.add(string[i:i+length])
    return patterns
