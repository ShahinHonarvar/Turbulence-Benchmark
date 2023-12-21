
def palindromes_of_specific_lengths(s):
    s = s[30:85]
    palindromes = set()
    for length in range(12,21):
        for i in range(len(s) - length + 1):
            substring = s[i:i+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
