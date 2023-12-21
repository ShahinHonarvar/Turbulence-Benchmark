
def palindromes_of_specific_lengths(s):
    s = s[12:93]
    palindromes = set()
    for length in range(17, 67):
        for idx in range(len(s) - length + 1):
            substring = s[idx:idx+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
