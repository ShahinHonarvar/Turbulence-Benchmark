
def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[24:85]
    for length in range(21, 32):
        for i in range(len(s) - length + 1):
            substring = s[i:i+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
