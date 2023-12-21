
def palindromes_of_specific_lengths(s):
    s = s[31:92].lower()
    palindromes = set()
    for l in range(50, 54):
        for i in range(len(s) - l + 1):
            substring = s[i:i+l]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
