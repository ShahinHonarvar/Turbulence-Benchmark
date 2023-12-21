
def palindromes_of_specific_lengths(s):
    s = s[45:99]
    palindromes = set()
    for i in range(len(s)-39):
        for j in range(40, min(48, len(s) - i + 1)):
            substring = s[i:i+j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
