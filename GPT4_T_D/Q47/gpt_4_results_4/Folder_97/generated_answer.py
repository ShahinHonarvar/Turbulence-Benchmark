
def palindromes_of_specific_lengths(s):
    import re
    s = s[28:95]
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    palindromes = set()
    for length in range(38, 50): 
        for i in range(len(s) - length + 1):
            substr = s[i : i + length]
            if substr == substr[::-1]: 
                palindromes.add(substr)
    return palindromes
